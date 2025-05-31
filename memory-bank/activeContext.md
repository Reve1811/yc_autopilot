# Active Context

## Current Work Focus

- [ ] メモリーバンクファイルの読み込み
- [ ] スクリーンショット取得の関数化
  - [x] yc_autopilot/screen_shot_manager.pyを作成する
  - [x] 上記のファイルに以下の実装を追加する
    - [x] yc_autopilot/config.pyをimportからSCREEN_SHOT_DIRをimportする
    - [x] get_screen_shot_path_by_image_name()関数を作成する
      - [x] 引数はimage_name: str
      - [x] 戻り値はstr
      - [x] os.path.joinを使い，SCREEN_SHOT_DIRと引数のimage_nameを結合し，それをreturnする


## Next Steps
- [ ] 村フェイズの自動化
  - [ ] パーティ初期化
  - [ ] 聖なる儀式解放までの自動化

## Active Decisions and Considerations
