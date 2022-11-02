import argparse

def dictionary(path, id):
    
    ##データの読み込み
    with open(path,encoding="utf-8") as f:
        text = [s.strip() for s in f.readlines()]
    
    ##行数の取得
    length = len(text)

    ##以下与えられたidによって分岐
    ##idが0の場合はid指定なしとして扱う
    if id == 0:
        ##id指定がないため、全行表示する
        for i in range(length):
            print("{}:{}".format(i+1,text[i]))

    else:
        ##指定されたidのみ表示する
        print("{}:{}".format(id,text[id-1]))

## コマンドライン引数の設定
if __name__=='__main__':
    parser = argparse.ArgumentParser(description='テキストファイルの単語をID付きで出力するプログラム')
    parser.add_argument("path", default="dictionary-data.csv", help="単語ファイル名")
    parser.add_argument("id", type=int, default=0, help="表示したい単語のID")
    args = parser.parse_args( )
    dictionary(args.path, args.id)
