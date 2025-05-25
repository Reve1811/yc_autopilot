# Active Context

## Current Work Focus

- [x] メモリーバンクファイルの読み込み
- [x] ファイル・関数の整理
  - [x] yc_autopilotというディレクトリを作成してください
  - [x] yc_autopilot\initializer.pyというファイルを作成してください
  - [x] main.pyにある以下の関数をinitialize.pyに移動してください（importなども含む）
    - [x] activate_main_tab()
    - [x] adjust_window_position()
    - [x] resizse_window()
    - [x] is_main_tab_active()  

## Next Steps

- [x] 共通関数
  - [x] マウス操作の共通関数作成
  - [x] yc_autopilot\manipulator.pyを作成する
  - [x] manipulator.pyに以下の関数を実装する
    - [x] mouse_click_by_image
      - [x] 引数は image_name: str とする
      - [x] 指定した名前の画像をscreen_shotディレクトリから探す
      - [x] 画像があったら，その画像に相当する位置をクリックし，Trueを返す
      - [x] 画像がなかったら，ないことをコンソールに出力し，Falseを返す
    - [x] enter_key_board
      - [x] 引数は key_name: str, x: int, y: int とする
      - [x] x, yの位置にマウスポインターを移動する
- [ ] 村フェイズの自動化
  - [ ] パーティ初期化
  - [ ] 聖なる儀式解放までの自動化

## Active Decisions and Considerations
