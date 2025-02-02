"""This module is for the translation mapping data of the
following document:

Document file: animation_return_value.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {
    ##################################################
    "# Each animation interface return value": "# 各アニメーションのインターフェイスの返却値",
    ##################################################
    "This page explains each animation interface, such as the `animation_move`\\, return value (`AnimationBase` instance).": "このページでは`animation_move`などの各アニメーションのインターフェイスの返却値について説明します。",  # noqa
    ##################################################
    "## Each interface returns the subclass instance of the AnimationBase": "## 各インターフェイスはAnimationBaseのサブクラスのインスタンスを返却します",  # noqa
    ##################################################
    "Each animation interface returns the subclass instance of the `AnimationBase`\\. So, for example, the `animation_move` interface returns the `AnimationMove` instance, and the `animation_x` interface  returns the `AnimationX` instance.": "各アニメーション関係のインターフェイスは`AnimationBase`のサブクラスのインスタンスを返却します。例えば`animation_move`インターフェイスであれば`AnimationMove`クラスのインスタンスを返却し、`animation_x`であれば`AnimationX`クラスのインスタンスを返却します。",  # noqa
    ##################################################
    "The `AnimationBase` class has the standard animation interfaces, such as the `start` (method to start animation), `animation_complete` (method to bind the animation completion event), `target` (property of the animation target).": "`AnimationBase`クラスはアニメーションの開始用の`start`メソッドやアニメーション終了時のイベント登録用の`animation_complete`メソッドなどの基本的な共通のアニメーション関係のインターフェイスを持っています。",  # noqa
    ##################################################
    "## Basic usage": "## 基本的な使い方",
    ##################################################
    "Each return value class is in the apysc package (e.g., `ap.AnimationMove`). Therefore, you can set the type annotation with it.": "返却された各値のクラスはapyscのパッケージに含まれています（例: `ap.AnimationMove`など）。そのためそれらを使用して型アノテーションを行うことができます。",  # noqa
    ##################################################
    "The following code example uses the `animation_x` method interface. And You get an `AnimationX` instance to start and bind the animation completion event with it.": "以下のコード例では`animation_x`メソッドを使用しており、返却値として`AnimationX`クラスのインスタンスを受け取っています。加えて`AnimationX`クラスのインスタンスを参照してアニメーション完了時のイベントを設定したりアニメーションを開始したり等を行っています。",  # noqa
    ##################################################
    '```py\n# runnable\nimport apysc as ap\n\nDURATION: int = 1000\n\n\ndef on_animation_complete_1(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    animation_x: ap.AnimationX = rectangle.animation_x(x=50, duration=DURATION)\n    animation_x.animation_complete(on_animation_complete_2)\n    animation_x.start()\n\n\ndef on_animation_complete_2(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    animation_x: ap.AnimationX = rectangle.animation_x(x=100, duration=DURATION)\n    animation_x.animation_complete(on_animation_complete_1)\n    animation_x.start()\n\n\nap.Stage(\n    stage_width=200, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nanimation_x: ap.AnimationX = rectangle.animation_x(x=100, duration=DURATION)\nanimation_x.animation_complete(on_animation_complete_1)\nanimation_x.start()\n\nap.save_overall_html(dest_dir_path="./animation_return_value_basic_usage/")\n```': '```py\n# runnable\nimport apysc as ap\n\nDURATION: int = 1000\n\n\ndef on_animation_complete_1(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    animation_x: ap.AnimationX = rectangle.animation_x(x=50, duration=DURATION)\n    animation_x.animation_complete(on_animation_complete_2)\n    animation_x.start()\n\n\ndef on_animation_complete_2(e: ap.AnimationEvent[ap.Rectangle], options: dict) -> None:\n    """\n    The handler that the animation calls when its end.\n\n    Parameters\n    ----------\n    e : ap.AnimationEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rectangle: ap.Rectangle = e.this.target\n    animation_x: ap.AnimationX = rectangle.animation_x(x=100, duration=DURATION)\n    animation_x.animation_complete(on_animation_complete_1)\n    animation_x.start()\n\n\nap.Stage(\n    stage_width=200, stage_height=150, background_color="#333", stage_elem_id="stage"\n)\nsprite: ap.Sprite = ap.Sprite()\nsprite.graphics.begin_fill(color="#0af")\nrectangle: ap.Rectangle = sprite.graphics.draw_rect(x=50, y=50, width=50, height=50)\nanimation_x: ap.AnimationX = rectangle.animation_x(x=100, duration=DURATION)\nanimation_x.animation_complete(on_animation_complete_1)\nanimation_x.start()\n\nap.save_overall_html(dest_dir_path="./animation_return_value_basic_usage/")\n```',  # noqa
}
