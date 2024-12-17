import tkinter as tk
from tkinter import messagebox

# 秘密道具リスト
secret_tools = {
    "どこでもドア": "どこへでも一瞬で行けるドア。新しい環境でリフレッシュしよう！",
    "タケコプター": "自由に空を飛べるヘリコプター。視点を変えてみるのもいいかもね！",
    "もしもボックス": "もしもの世界を試せる電話ボックス。違う選択肢を考えてみよう！",
    "タイムマシン": "過去や未来を旅できるマシン。時間が解決してくれることもあるよ。",
    "ほんやくコンニャク": "どんな言葉も翻訳できる食品。コミュニケーションで解決しよう！",
    "スモールライト": "物を小さくするライト。悩みも少し小さく見えるかも？",
    "ビッグライト": "物を大きくするライト。自分の可能性を広げてみよう！",
    "どこでもカメラ": "どんな場所でも写真を撮ることができるカメラ。思い出を残したり、証拠を集めよう！",
    "ドラえもんのひみつ帳": "あらゆる知識が詰まった本。困ったときの解決法が書かれているよ！",
    "マジックボックス": "箱の中に何でも入れられる、不思議なボックス。荷物の整理も簡単にできる！",
    "しんせつなロボット": "どんなに忙しくても、あなたを手伝ってくれるロボット。サポートが必要な時に大活躍！",
    "エアコンマット": "どんな場所でも温度を快適に調整できるマット。暑さも寒さも気にせず快適に！",
    "アンキパン": "記憶力がアップするパン。勉強や記憶に苦労している人に♪",
    "お医者さんカバン": "体の予防・治療ができるカバン。健康の悩みも解決！",
    "グルメテーブルかけ": "何も出てくるテーブル布。食事の悩みもこれで解決！",
    "フエール銀行": "お金の心配も、自動で積み立てる銀行。頑張って貯金しよう！",
    "夢見るガス": "夢の世界を見せてくれるガス。未来の自分を想像してみて！"
}

# 悩みに基づいて秘密道具を提案する関数
def suggest_tool_based_on_problem(problem):
    problem = problem.lower()
    if "人間関係" in problem or "コミュニケーション" in problem:
        return "ほんやくコンニャク", secret_tools["ほんやくコンニャク"]
    elif "迷う" in problem or "選択肢" in problem:
        return "もしもボックス", secret_tools["もしもボックス"]
    elif "時間" in problem or "過去" in problem or "未来" in problem:
        return "タイムマシン", secret_tools["タイムマシン"]
    elif "成長" in problem or "可能性" in problem:
        return "ビッグライト", secret_tools["ビッグライト"]
    elif "勉強" in problem or "記憶" in problem:
        return "アンキパン", secret_tools["アンキパン"]
    elif "健康" in problem or "体調" in problem:
        return "お医者さんカバン", secret_tools["お医者さんカバン"]
    elif "お金" in problem or "貯金" in problem:
        return "フエール銀行", secret_tools["フエール銀行"]
    elif "食事" in problem or "料理" in problem:
        return "グルメテーブルかけ", secret_tools["グルメテーブルかけ"]
    elif "夢" in problem or "未来" in problem:
        return "夢見るガス", secret_tools["夢見るガス"]
    else:
        return None, None

# GUIアプリケーションの作成
class DoraemonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ドラえもんの秘密道具提案アプリ")

        # ラベル
        self.label = tk.Label(root, text="未来の猫型ロボットが来たよ！何か悩み事がある？", font=("Arial", 14))
        self.label.pack(pady=10)

        # テキスト入力欄
        self.problem_entry = tk.Entry(root, width=50)
        self.problem_entry.pack(pady=5)

        # 提案ボタン
        self.suggest_button = tk.Button(root, text="秘密道具を提案して！", command=self.suggest_tool)
        self.suggest_button.pack(pady=5)

        # 結果表示ラベル
        self.result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=400)
        self.result_label.pack(pady=10)

    def suggest_tool(self):
        problem = self.problem_entry.get().strip()
        if not problem:
            messagebox.showinfo("入力エラー", "悩みを入力してください！")
            return

        tool, advice = suggest_tool_based_on_problem(problem)
        if tool:
            result_text = f"提案する秘密道具は…『{tool}』だよ！\n{advice}"
            self.result_label.config(text=result_text)
        else:
            self.result_label.config(text="ごめんね、その悩みに合う秘密道具が見つからなかったよ\nもう一度入力してみてね！")

# メイン処理
if __name__ == "__main__":
    root = tk.Tk()
    app = DoraemonApp(root)
    root.mainloop()
