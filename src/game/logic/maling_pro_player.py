from game.logic.base import BaseLogic
from game.models import GameObject, Board, Position
from game.util import get_direction, position_equals


class MalingProPlayer(BaseLogic):
    def __init__(self):
        self.goal_position: Position = None
        self.detik_detik_kematian = False

        print("Maling Pro Player siap maling diamond sebanyak-banyaknya!")

    def next_move(self, board_bot: GameObject, board: Board):
        lokasi_base = board_bot.properties.base
        lokasi_bot_kita = board_bot.position
        jumlah_diamond_di_inventory = board_bot.properties.diamonds
        jumlah_waktu_yang_tersisa = board_bot.properties.milliseconds_left
        jumlah_maksimal_diamond_di_inventory = board_bot.properties.inventory_size

        diamonds = board.diamonds
        bots = board.bots

        # Jika bot berada di detik-detik kematian, maka fokus untuk kembali ke base
        if self.detik_detik_kematian:
            return get_direction(
                lokasi_bot_kita.x,
                lokasi_bot_kita.y,
                lokasi_base.x,
                lokasi_base.y,
            )

        # Hitung jarak dari lokasi bot kita ke base
        jarak_ke_base = abs(lokasi_bot_kita.x - lokasi_base.x) + abs(
            lokasi_bot_kita.y - lokasi_base.y
        )

        # Asumsikan untuk bergerak butuh 1 detik
        waktu_kembali_ke_base = jarak_ke_base * 1000

        # Jika waktu yang tersisa kurang dari atau sama dengan waktu untuk kembali ke base,
        # maka set detik_detik_kematian menjadi True
        if jumlah_waktu_yang_tersisa <= waktu_kembali_ke_base:
            self.goal_position = lokasi_base
            self.detik_detik_kematian = True

        # Jika inventory bot sudah penuh dengan diamond,
        # maka fokus untuk kembali ke base
        if jumlah_diamond_di_inventory >= jumlah_maksimal_diamond_di_inventory:
            self.goal_position = lokasi_base

        # Ini untuk mengecek apakah musuh berada di dekat kita
        # Jika ada musuh di dekat kita, maka bot akan melakukan tackle
        # Sebagai bentuk bertahan diri, dibandingkan bot kita yang kena tackle
        musuh_berada_di_dekat = False
        lokasi_musuh = None
        for bot in bots:
            if bot.id != board_bot.id:
                dx = abs(bot.position.x - lokasi_bot_kita.x)
                dy = abs(bot.position.y - lokasi_bot_kita.y)
                if (dx == 1 and dy == 0) or (dx == 0 and dy == 1):
                    musuh_berada_di_dekat = True
                    lokasi_musuh = bot.position
                    break

        # Jika ada musuh di dekat kita, maka fokus untuk tackle musuh tersebut
        if musuh_berada_di_dekat:
            self.goal_position = lokasi_musuh

        # Jika sudah sampai tujuan maka reset goal_position
        if self.goal_position and position_equals(self.goal_position, lokasi_bot_kita):
            self.goal_position = None

        # Jika bot masih belum memiliki tujuan, maka cari diamond dengan densitas tertinggi
        # dan diamond yang paling dekat dengan base
        if self.goal_position is None:
            density_maksimal = 0
            target_diamond = None

            # Mulai mencari diamond dengan densitas tertinggi dan paling dekat dengan base
            for diamond in diamonds:
                # Hitung jarak dari diamond ke bot kita
                jarak_bot = abs(diamond.position.x - lokasi_bot_kita.x) + abs(
                    diamond.position.y - lokasi_bot_kita.y
                )

                # Hitung jarak dari diamond ke base
                jarak_base = abs(diamond.position.x - lokasi_base.x) + abs(
                    diamond.position.y - lokasi_base.y
                )

                # Total jarak dari bot ke diamond dan dari diamond ke base
                total_jarak = jarak_bot + jarak_base

                # Cari tau poin yang dimiliki diamond
                diamond_points = (
                    diamond.properties.points if diamond.properties.points else 1
                )

                # Hitung densitas diamond berdasarkan poin dan total jarak
                density = diamond_points / (total_jarak + 1)

                # Jika densitas diamond lebih tinggi dari densitas maksimal yang ditemukan,
                # maka set diamond tersebut sebagai target dan update densitas maksimal
                if density > density_maksimal:
                    density_maksimal = density
                    target_diamond = diamond

            # Jika ada diamond yang ditemukan dengan densitas tertinggi,
            # maka set goal_position ke posisi diamond tersebut
            # Jika tidak ada diamond yang ditemukan, maka set goal_position ke base
            if target_diamond:
                self.goal_position = target_diamond.position
            else:
                self.goal_position = lokasi_base

        # Selalu return arah menuju tujuan
        return get_direction(
            lokasi_bot_kita.x,
            lokasi_bot_kita.y,
            self.goal_position.x,
            self.goal_position.y,
        )
