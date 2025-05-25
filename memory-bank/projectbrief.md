# Project Brief
- このプロジェクトはYour Chronicleを自動化することを目的としています．
- Your Chronicleは放置型RPGに属するPCゲームです．
- 操作はマウスクリックとキーボード操作のみです．
## Project Goals

- Your Chronicleを自動化するためのpythonプログラムを作成することが目的です
- 具体的な指示は個別のタスクとして提示します．

## Core Requirements

- 指定されたボタンを自動操作する機能
- 操作記録をコンソールに出力する機能

## directory structure
yc_autopilot/
├── memory-bank/          # ClineのMemory Bankファイル群
│   ├── projectbrief.md
│   ├── systemPatterns.md
│   └── ...
├── yc_autopilot/ ソースコード
    ├── screen_shot/ # ボタンや選択状況を調べるためのスクリーンショット
    ├── initializer.py/ # 初期化用のコード
    ├── __main__.py/ # エントリーポイント
    └── ...
