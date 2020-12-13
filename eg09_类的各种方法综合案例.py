class Game:
    # 历史最高分
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("帮助信息：让僵尸进入大门")

    @classmethod
    def show_top_score(cls):
        print("历史最高记录：{}".format(cls.top_score))

    def start_game(self):
        print("玩家 - {}开始游戏啦".format(self.player_name))


# 查看游戏的帮助信息
Game.show_help()
# 查看历史最高分
Game.show_top_score()
# 创建游戏对象
game = Game("李丹")
game.start_game()
