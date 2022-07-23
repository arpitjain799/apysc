"""This module is for the translation mapping data of the
following document:

Document file: animation_fill_color.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# animation_fill_color interface": "# animation_fill_color インターフェイス",
    ##################################################
    "This page explains the `animation_fill_color` method interface.": "このページでは`animation_fill_color`メソッドのインターフェイスについて説明します。",  # noqa
    ##################################################
    "## What interface is this?": "## インターフェイス概要",
    ##################################################
    "The `animation_fill_color` method interface creates an `ap.AnimationFillColor` instance. You can animate fill color with it.": "`animation_fill_color`メソッドのインターフェイスは`ap.AnimationFillColor`クラスのインスタンスを生成します。そのインスタンスを使って塗りのアニメーションを行うことができます。",  # noqa
    ##################################################
    "This interface exists on a `GraphicsBase` subclass, such as the `Rectangle` or `Circle` class.": "このインターフェイスは`Rectangle`や`Circle`クラスなどの`GraphicsBase`のサブクラスで存在します。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "The following example sets the fill color animation (from cyan color `#0af` to magenta `#f0a`) with the `animation_fill_color` method:": "以下のコード例では`animation_fill_color`メソッドを使って塗りの色をシアン（`#0af`）からマゼンタ（`#f0a`）へとアニメーションさせています。",  # noqa
    ##################################################
    "```py\n# runnable\nimport apysc as ap\n\nDURATION: int = 1000\n\n\ndef on_animation_complete_1(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    \"\"\"\n    The handler that animation calls when its end.\n\n    Parameters\n    ----------\n    e : AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    \"\"\"\n    rectangle: ap.Rectangle = e.this.target\n    rectangle.animation_fill_color(\n        fill_color=\"#0af\",\n        duration=DURATION,\n    ).animation_complete(on_animation_complete_2).start()\n\n\ndef on_animation_complete_2(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    \"\"\"\n    The handler that animation calls when its end.\n\n    Parameters\n    ----------\n    e : AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    \"\"\"\n    rectangle: ap.Rectangle = e.this.target\n    rectangle.animation_fill_color(\n        fill_color=\"#f0a\",\n        duration=DURATION,\n    ).animation_complete(on_animation_complete_1).start()\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color=\"#333\", stage_elem_id=\"stage\"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\"#0af\")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.animation_fill_color(\n    fill_color=\"#f0a\",\n    duration=DURATION,\n).animation_complete(on_animation_complete_1).start()\n\nap.save_overall_html(dest_dir_path=\"./animation_fill_color_basic_usage/\")\n```": "```py\n# runnable\nimport apysc as ap\n\nDURATION: int = 1000\n\n\ndef on_animation_complete_1(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    \"\"\"\n    The handler that animation calls when its end.\n\n    Parameters\n    ----------\n    e : AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    \"\"\"\n    rectangle: ap.Rectangle = e.this.target\n    rectangle.animation_fill_color(\n        fill_color=\"#0af\",\n        duration=DURATION,\n    ).animation_complete(on_animation_complete_2).start()\n\n\ndef on_animation_complete_2(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    \"\"\"\n    The handler that animation calls when its end.\n\n    Parameters\n    ----------\n    e : AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    \"\"\"\n    rectangle: ap.Rectangle = e.this.target\n    rectangle.animation_fill_color(\n        fill_color=\"#f0a\",\n        duration=DURATION,\n    ).animation_complete(on_animation_complete_1).start()\n\n\nap.Stage(\n    stage_width=150, stage_height=150, background_color=\"#333\", stage_elem_id=\"stage\"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color=\"#0af\")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nrectangle.animation_fill_color(\n    fill_color=\"#f0a\",\n    duration=DURATION,\n).animation_complete(on_animation_complete_1).start()\n\nap.save_overall_html(dest_dir_path=\"./animation_fill_color_basic_usage/\")\n```",  # noqa
    ##################################################
    "## animation_fill_color API": "## animation_fill_color API",
    ##################################################
    "<span class=\"inconspicuous-txt\">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>": "<span class=\"inconspicuous-txt\">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>",  # noqa
    ##################################################
    "**[Interface summary]** Set the fill color animation setting.<hr>": "**[インターフェイス概要]** 塗りの色のアニメーションの設定を行います。.<hr>",  # noqa
    ##################################################
    "**[Parameters]**": "**[引数]**",
    ##################################################
    "- `fill_color`: str or String": "- `fill_color`: str or String",
    ##################################################
    "  - The final fill color (hex color code) of the animation.": "  - アニメーションの最終的な塗りの色（16進数の色の文字列）。",  # noqa
    ##################################################
    "- `duration`: Int or int, default 3000": "- `duration`: Int or int, default 3000",
    ##################################################
    "  - Milliseconds before an animation ends.": "  - アニメーション完了までのミリ秒。",
    ##################################################
    "- `delay`: Int or int, default 0": "- `delay`: Int or int, default 0",
    ##################################################
    "  - Milliseconds before an animation starts.": "  - アニメーション開始までの遅延時間のミリ秒。",
    ##################################################
    "- `easing`: Easing, default Easing.LINEAR": "- `easing`: Easing, default Easing.LINEAR",  # noqa
    ##################################################
    "  - Easing setting.": "  - イージング設定。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Returns]**": "**[返却値]**",
    ##################################################
    "- `animation_fill_color`: AnimationFillColor": "- `animation_fill_color`: AnimationFillColor",  # noqa
    ##################################################
    "  - Created animation setting instance.": "  - 生成されたアニメーションのインスタンス。",
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[Notes]**": "**[特記事項]**",
    ##################################################
    "To start this animation, you need to call the `start` method of the returned instance.<hr>": "アニメーションを開始するには返却されたインスタンスの`start`メソッドを呼び出す必要があります。<hr>",  # noqa
    ##################################################
    "**[Examples]**": "**[コードサンプル]**",
    ##################################################
    "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.animation_fill_color(\n...     fill_color=\'#f0a\',\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n```": "```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> sprite: ap.Sprite = ap.Sprite()\n>>> sprite.graphics.begin_fill(color=\'#0af\')\n>>> rectangle: ap.Rectangle = sprite.graphics.draw_rect(\n...     x=50, y=50, width=50, height=50)\n>>> _ = rectangle.animation_fill_color(\n...     fill_color=\'#f0a\',\n...     duration=1500,\n...     easing=ap.Easing.EASE_OUT_QUINT,\n... ).start()\n```",  # noqa
    ##################################################
    "<hr>": "<hr>",
    ##################################################
    "**[References]**": "**[関連資料]**",
    ##################################################
    "- [Animation interfaces duration setting document](https://simon-ritchie.github.io/apysc/en/animation_duration.html)": "- [各アニメーションインターフェイスの duration （アニメーション時間）設定](https://simon-ritchie.github.io/apysc/en/jp_animation_duration.html)",  # noqa
    ##################################################
    "- [Animation interfaces delay setting document](https://simon-ritchie.github.io/apysc/en/animation_delay.html)": "- [各アニメーションインターフェイスの delay （遅延時間）設定](https://simon-ritchie.github.io/apysc/en/jp_animation_delay.html)",  # noqa
    ##################################################
    "- [Each animation interface return value document](https://simon-ritchie.github.io/apysc/en/animation_return_value.html)": "- [各アニメーションインターフェイスの返却値](https://simon-ritchie.github.io/apysc/en/jp_animation_return_value.html)",  # noqa
    ##################################################
    "- [Sequential animation setting document](https://simon-ritchie.github.io/apysc/en/sequential_animation.html)": "- [連続したアニメーション設定](https://simon-ritchie.github.io/apysc/en/jp_sequential_animation.html)",  # noqa
    ##################################################
    "- [animation_parallel interface document](https://simon-ritchie.github.io/apysc/en/animation_parallel.html)": "- [animation_parallel （並列アニメーション設定）のインターフェイス](https://simon-ritchie.github.io/apysc/en/jp_animation_parallel.html)",  # noqa
    ##################################################
    "- [Easing enum document](https://simon-ritchie.github.io/apysc/en/easing_enum.html)": "- [イージングのenum](https://simon-ritchie.github.io/apysc/en/jp_easing_enum.html)",  # noqa
}
