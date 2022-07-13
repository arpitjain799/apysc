"""This module is for the translation mapping data of the
following document:

Document file: line.md
Language: jp
"""

from typing import Dict

MAPPING: Dict[str, str] = {

    '# Line class':
    '# Line クラス',

    'This page explains the `Line` class.':
    'このページでは`Line`クラスについて説明します。',

    '## What class is this?':
    '## クラス概要',

    'The `Line` class creates a straight-line vector graphics object.':
    '`Line`クラスは直線のベクターグラフィックスを生成します。',

    '## Basic usage':
    '## 基本的な使い方',

    'The `Line` class constructor requires the `start_point` and `end_point` arguments.':  # noqa
    '`Line`クラスのコンストラクタでは`start_point`や`end_point`の引数指定を必要とします。',

    'The constructor also accepts each style\'s argument, such as the `line_color`.':  # noqa
    'コンストラクタは`line_color`などのスタイル設定の引数も受け付けます。',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50),\n    line_color=\'#0af\', line_thickness=5)\n\nap.save_overall_html(\n    dest_dir_path=\'line_basic_usage/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50),\n    line_color=\'#0af\', line_thickness=5)\n\nap.save_overall_html(\n    dest_dir_path=\'line_basic_usage/\')\n```',  # noqa

    '## Note of the draw_line or other interfaces':
    '## draw_line や他の各インターフェイスの特記事項',

    'You can also create a line instance with the `draw_line` interface (or the other interfaces, such as the `draw_dotted_line`).':  # noqa
    '`draw_line`や`draw_dotted_line`などの他のインターフェイスを使う形でも直線のインスタンスを生成することができます。',  # noqa

    'Please see also:':
    '関連資料:',

    '- [Graphics class draw_line interface](graphics_draw_line.md)':
    '- [Graphics クラスの draw_line (線の描画)のインターフェイス](jp_graphics_draw_line.md)',

    '- [Graphics class draw_dotted_line interface](graphics_draw_dotted_line.md)':  # noqa
    '- [Graphics クラスの draw_dotted_line (点線の描画)のインターフェイス](jp_graphics_draw_dotted_line.md)',  # noqa

    '- [Graphics class draw_dashed_line interface](graphics_draw_dashed_line.md)':  # noqa
    '- [Graphics クラスの draw_dashed_line (破線の描画)のインターフェイス](jp_graphics_draw_dashed_line.md)',  # noqa

    '- [Graphics class draw_round_dotted_line interface](graphics_draw_round_dotted_line.md)':  # noqa
    '- [Graphics クラスの draw_round_dotted_line (点線(丸)の描画)のインターフェイス](jp_graphics_draw_round_dotted_line.md)',  # noqa

    '- [Graphics class draw_dash_dotted_line interface](graphics_draw_dash_dotted_line.md)':  # noqa
    '- [Graphics クラスの draw_dash_dotted_line (一点鎖線の描画)のインターフェイス](jp_graphics_draw_dash_dotted_line.md)',  # noqa

    '## x property interface example':
    '## x属性のインターフェイス例',

    'The `x` property updates or gets the instance\'s x-coordinate:':
    '`x`属性ではX座標の値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50),\n    line_color=\'#0af\', line_thickness=5)\nline.x = ap.Int(100)\n\nap.save_overall_html(\n    dest_dir_path=\'line_x/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50),\n    line_color=\'#0af\', line_thickness=5)\nline.x = ap.Int(100)\n\nap.save_overall_html(\n    dest_dir_path=\'line_x/\')\n```',  # noqa

    'Notes: this attribute\'s value becomes the same as the arguments\' minimum point value.':  # noqa
    '特記事項: この属性の値は引数の座標の最小値と同値になります。',

    '## y property interface example':
    '## y属性のインターフェイス例',

    'The `y` property updates or gets the instance\'s y-coordinate:':
    '`y`属性ではY座標の値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50),\n    line_color=\'#0af\', line_thickness=5)\nline.y = ap.Int(80)\n\nap.save_overall_html(\n    dest_dir_path=\'line_y/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50),\n    line_color=\'#0af\', line_thickness=5)\nline.y = ap.Int(80)\n\nap.save_overall_html(\n    dest_dir_path=\'line_y/\')\n```',  # noqa

    'Notes: this attribute\'s value becomes the same as the arguments\' minimum point value.':  # noqa
    '特記事項: この属性の値は引数の座標の最小値と同値になります。',

    '## line_color property interface example':
    '## line_color属性のインターフェイス例',

    'The `line_color` property updates or gets the instance\'s line color:':
    '`line_color`属性では線の色の値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50), line_thickness=5)\nline.line_color = ap.String(\'#f0a\')\n\nap.save_overall_html(\n    dest_dir_path=\'line_line_color/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50), line_thickness=5)\nline.line_color = ap.String(\'#f0a\')\n\nap.save_overall_html(\n    dest_dir_path=\'line_line_color/\')\n```',  # noqa

    '## line_alpha property interface example':
    '## line_alpha属性のインターフェイス例',

    'The `line_alpha` property updates or gets the instance\'s line alpha (opacity):':  # noqa
    '`line_alpha`属性では線の透明度の値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50),\n    line_color=\'#0af\', line_thickness=5)\nline.line_alpha = ap.Number(0.3)\n\nap.save_overall_html(\n    dest_dir_path=\'line_line_alpha/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50),\n    line_color=\'#0af\', line_thickness=5)\nline.line_alpha = ap.Number(0.3)\n\nap.save_overall_html(\n    dest_dir_path=\'line_line_alpha/\')\n```',  # noqa

    '## line_thickness property interface example':
    '## line_thickness属性のインターフェイス例',

    'The `line_thickness` property updates or gets the instance\'s line thickness (line width):':  # noqa
    '`line_thickness`属性では線の幅の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50),\n    line_color=\'#0af\')\nline.line_thickness = ap.Int(10)\n\nap.save_overall_html(\n    dest_dir_path=\'line_line_thickness/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50),\n    line_color=\'#0af\')\nline.line_thickness = ap.Int(10)\n\nap.save_overall_html(\n    dest_dir_path=\'line_line_thickness/\')\n```',  # noqa

    '## line_dot_setting property interface example':
    '## line_dot_setting属性のインターフェイス例',

    'The `line_dot_setting` property updates or gets the instance\'s line dot-style setting:':  # noqa
    '`line_dot_setting`属性では点線のスタイル設定の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50),\n    line_color=\'#0af\', line_thickness=3)\nline.line_dot_setting = ap.LineDotSetting(dot_size=3)\n\nap.save_overall_html(\n    dest_dir_path=\'line_line_dot_setting/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50),\n    line_color=\'#0af\', line_thickness=3)\nline.line_dot_setting = ap.LineDotSetting(dot_size=3)\n\nap.save_overall_html(\n    dest_dir_path=\'line_line_dot_setting/\')\n```',  # noqa

    '## line_dash_setting property interface example':
    '## line_dash_setting属性のインターフェイス例',

    'The `line_dash_setting` property updates or gets the instance\'s line dash-style setting:':  # noqa
    '`line_dash_setting`属性では破線のスタイル設定の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50),\n    line_color=\'#0af\', line_thickness=3)\nline.line_dash_setting = ap.LineDashSetting(\n    dash_size=6, space_size=2)\n\nap.save_overall_html(\n    dest_dir_path=\'line_line_dash_setting/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50),\n    line_color=\'#0af\', line_thickness=3)\nline.line_dash_setting = ap.LineDashSetting(\n    dash_size=6, space_size=2)\n\nap.save_overall_html(\n    dest_dir_path=\'line_line_dash_setting/\')\n```',  # noqa

    '## line_round_dot_setting property interface example':
    '## line_round_dot_setting属性のインターフェイス例',

    'The `line_round_dot_setting` property updates or gets the instance\'s line round dot-style setting:':  # noqa
    '`line_round_dot_setting`属性では丸ドット線のスタイル設定の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50),\n    line_color=\'#0af\')\nline.line_round_dot_setting = ap.LineRoundDotSetting(\n    round_size=5, space_size=3)\n\nap.save_overall_html(\n    dest_dir_path=\'line_line_round_dot_setting/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50),\n    line_color=\'#0af\')\nline.line_round_dot_setting = ap.LineRoundDotSetting(\n    round_size=5, space_size=3)\n\nap.save_overall_html(\n    dest_dir_path=\'line_line_round_dot_setting/\')\n```',  # noqa

    '## line_dash_dot_setting property interface example':
    '## line_dash_dot_setting属性のインターフェイス例',

    'The `line_dash_dot_setting` property updates or gets the instance\'s dash-dotted line style setting:':  # noqa
    '`line_dash_dot_setting`属性では一点鎖線のスタイル設定の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50),\n    line_color=\'#0af\', line_thickness=3)\nline.line_dash_dot_setting = ap.LineDashDotSetting(\n    dot_size=2, dash_size=5, space_size=2)\n\nap.save_overall_html(\n    dest_dir_path=\'line_line_dash_dot_setting/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=50),\n    end_point=ap.Point2D(x=150, y=50),\n    line_color=\'#0af\', line_thickness=3)\nline.line_dash_dot_setting = ap.LineDashDotSetting(\n    dot_size=2, dash_size=5, space_size=2)\n\nap.save_overall_html(\n    dest_dir_path=\'line_line_dash_dot_setting/\')\n```',  # noqa

    '## rotation_around_center property interface example':
    '## rotation_around_center属性のインターフェイス例',

    'The `rotation_around_center` property updates or gets the instance\'s rotation value (0 to 359) from the center point:':  # noqa
    '`rotation_around_center`属性ではインスタンスの中央座標での回転量（0～359）の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=40),\n    end_point=ap.Point2D(x=150, y=60),\n    line_color=\'#0af\',\n    line_thickness=3)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    line.rotation_around_center += 1\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(\n    dest_dir_path=\'line_rotation_around_center/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=40),\n    end_point=ap.Point2D(x=150, y=60),\n    line_color=\'#0af\',\n    line_thickness=3)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    line.rotation_around_center += 1\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(\n    dest_dir_path=\'line_rotation_around_center/\')\n```',  # noqa

    '## set_rotation_around_point and get_rotation_around_point methods interfaces example':  # noqa
    '## set_rotation_around_pointとget_rotation_around_pointメソッドのインターフェイス例',

    'The `set_rotation_around_point` method updates the instance\'s rotation value (0 to 359) from a specified point.':  # noqa
    '`set_rotation_around_point`メソッドは指定された座標からのインスタンスの回転量（0～359）を更新します。',

    'Similarly, the `get_rotation_around_point` method gets the instance\'s rotation value (0 to 359) from a specified point:':  # noqa
    '同様に、`get_rotation_around_point`メソッドでは指定された座標のインスタンスの回転量（0～359）を取得します:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=40),\n    end_point=ap.Point2D(x=150, y=60),\n    line_color=\'#0af\',\n    line_thickness=3)\nx: ap.Int = ap.Int(100)\ny: ap.Int = ap.Int(100)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rotation: ap.Int = line.get_rotation_around_point(\n        x=x, y=y)\n    rotation += 1\n    line.set_rotation_around_point(\n        rotation=rotation, x=x, y=y)\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(\n    dest_dir_path=\'line_set_rotation_around_point/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=40),\n    end_point=ap.Point2D(x=150, y=60),\n    line_color=\'#0af\',\n    line_thickness=3)\nx: ap.Int = ap.Int(100)\ny: ap.Int = ap.Int(100)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    rotation: ap.Int = line.get_rotation_around_point(\n        x=x, y=y)\n    rotation += 1\n    line.set_rotation_around_point(\n        rotation=rotation, x=x, y=y)\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(\n    dest_dir_path=\'line_set_rotation_around_point/\')\n```',  # noqa

    '## flip_x property interface example':
    '## flip_x属性のインターフェイス例',

    'The `flip_x` property updates or gets the instance\'s flip-x (reflecting state) boolean value:':  # noqa
    '`flip_x`属性ではインスタンスのX軸の反転状況の真偽値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=40),\n    end_point=ap.Point2D(x=150, y=60),\n    line_color=\'#0af\',\n    line_thickness=3)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    line.flip_x = line.flip_x.not_\n\n\nap.Timer(on_timer, delay=1000).start()\nap.save_overall_html(\n    dest_dir_path=\'line_flip_x/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=40),\n    end_point=ap.Point2D(x=150, y=60),\n    line_color=\'#0af\',\n    line_thickness=3)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    line.flip_x = line.flip_x.not_\n\n\nap.Timer(on_timer, delay=1000).start()\nap.save_overall_html(\n    dest_dir_path=\'line_flip_x/\')\n```',  # noqa

    'Notes: Depending on the shape of the instance, this may be difficult to tell the difference between the x and y axes interfaces.':  # noqa
    '特記事項: インスタンスの形状によってはこのインターフェイスはX軸とY軸の各インターフェイスで違いが分かりづらいケースが発生します。',

    '## flip_y property interface example':
    '## flip_y属性のインターフェイス例',

    'The `flip_y` property updates or gets the instance\'s flip-y (reflecting state) boolean value:':  # noqa
    '`flip_y`属性ではインスタンスのX軸の反転状況の真偽値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=40),\n    end_point=ap.Point2D(x=150, y=60),\n    line_color=\'#0af\',\n    line_thickness=3)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    line.flip_y = line.flip_y.not_\n\n\nap.Timer(on_timer, delay=1000).start()\nap.save_overall_html(\n    dest_dir_path=\'line_flip_y/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=40),\n    end_point=ap.Point2D(x=150, y=60),\n    line_color=\'#0af\',\n    line_thickness=3)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    line.flip_y = line.flip_y.not_\n\n\nap.Timer(on_timer, delay=1000).start()\nap.save_overall_html(\n    dest_dir_path=\'line_flip_y/\')\n```',  # noqa

    'Notes: Depending on the shape of the instance, this may be difficult to tell the difference between the x and y axes interfaces.':  # noqa
    '特記事項: インスタンスの形状によってはこのインターフェイスはX軸とY軸の各インターフェイスで違いが分かりづらいケースが発生します。',

    '## skew_x property interface example':
    '## skew_x属性のインターフェイス例',

    'The `skew_x` property updates or gets the instance\'s skew-x (distortion) value:':  # noqa
    '`skew_x`属性ではインスタンスのX軸の歪みの値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=40),\n    end_point=ap.Point2D(x=150, y=60),\n    line_color=\'#0af\',\n    line_thickness=3)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    line.skew_x += 1\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(\n    dest_dir_path=\'line_skew_x/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=40),\n    end_point=ap.Point2D(x=150, y=60),\n    line_color=\'#0af\',\n    line_thickness=3)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    line.skew_x += 1\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(\n    dest_dir_path=\'line_skew_x/\')\n```',  # noqa

    'Notes: Depending on the shape of the instance, this may be difficult to tell the difference between the x and y axes interfaces.':  # noqa
    '特記事項: インスタンスの形状によってはこのインターフェイスはX軸とY軸の各インターフェイスで違いが分かりづらいケースが発生します。',

    '## skew_y property interface example':
    '## skew_y属性のインターフェイス例',

    'The `skew_y` property updates or gets the instance\'s skew-y (distortion) value:':  # noqa
    '`skew_y`属性ではインスタンスのY軸の歪みの値の更新もしくは取得を行えます:',

    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=40),\n    end_point=ap.Point2D(x=150, y=60),\n    line_color=\'#0af\',\n    line_thickness=3)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    line.skew_y += 1\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(\n    dest_dir_path=\'line_skew_y/\')\n```':  # noqa
    '```py\n# runnable\nimport apysc as ap\n\nap.Stage(\n    background_color=\'#333\',\n    stage_width=200,\n    stage_height=100,\n    stage_elem_id=\'stage\')\nline: ap.Line = ap.Line(\n    start_point=ap.Point2D(x=50, y=40),\n    end_point=ap.Point2D(x=150, y=60),\n    line_color=\'#0af\',\n    line_thickness=3)\n\n\ndef on_timer(e: ap.TimerEvent, options: dict) -> None:\n    """\n    The timer event handler.\n\n    Parameters\n    ----------\n    e : ap.TimerEvent\n        Event instance.\n    options : dict\n        Optional arguments dictionary.\n    """\n    line.skew_y += 1\n\n\nap.Timer(on_timer, delay=ap.FPS.FPS_60).start()\nap.save_overall_html(\n    dest_dir_path=\'line_skew_y/\')\n```',  # noqa

    'Notes: Depending on the shape of the instance, this may be difficult to tell the difference between the x and y axes interfaces.':  # noqa
    '特記事項: インスタンスの形状によってはこのインターフェイスはX軸とY軸の各インターフェイスで違いが分かりづらいケースが発生します。',

    '## Line class constructor API':
    '## Line クラスのコンストラクタのAPI',

    '<span class="inconspicuous-txt">Note: the document build script generates and updates this API document section automatically. Maybe this section is duplicated compared with previous sections.</span>':  # noqa
    '<span class="inconspicuous-txt">特記事項: このAPIドキュメントはドキュメントビルド用のスクリプトによって自動で生成・同期されています。そのためもしかしたらこの節の内容は前節までの内容と重複している場合があります。</span>',  # noqa

    '**[Interface summary]** Create a line vector graphic.<hr>':
    '**[インターフェイス概要]** 線のベクターグラフィックスを生成します。<hr>',

    '**[Parameters]**':
    '**[引数]**',

    '- `start_point`: Points2D':
    '- `start_point`: Points2D',

    '  - Line start point.':
    '  - 線の開始座標。',

    '- `end_point`: Points2D':
    '- `end_point`: Points2D',

    '  - Line end point.':
    '  - 線の終了座標。',

    '- `line_color`: str or String, default \'\'':
    '- `line_color`: str or String, default \'\'',

    '  - A line-color to set.':
    '  - 設定する線の色。',

    '- `line_alpha`: float or Number, default 1.0':
    '- `line_alpha`: float or Number, default 1.0',

    '  - A line-alpha to set.':
    '  - 設定する線の透明度。',

    '- `line_thickness`: int or Int, default 1':
    '- `line_thickness`: int or Int, default 1',

    '  - A line-thickness (line-width) to set.':
    '  - 設定の線幅。',

    '- `line_cap`: String or LineCaps or None, default None':
    '- `line_cap`: String or LineCaps or None, default None',

    '  - A line-cap setting to set.':
    '  - 設定する線の端のスタイル設定。',

    '- `line_dot_setting`: LineDotSetting or None, default None':
    '- `line_dot_setting`: LineDotSetting or None, default None',

    '  - A dot setting to set.':
    '  - 設定する点線のスタイル設定。',

    '- `line_dash_setting`: LineDashSetting or None, default None':
    '- `line_dash_setting`: LineDashSetting or None, default None',

    '  - A dash setting to set.':
    '  - 設定する破線のスタイル設定。',

    '- `line_round_dot_setting`: LineRoundDotSetting or None, default None':
    '- `line_round_dot_setting`: LineRoundDotSetting or None, default None',

    '  - A round-dot setting to set.':
    '  - 設定する丸ドットのスタイル設定。',

    '- `line_dash_dot_setting`: LineDashDotSetting or None, default None':
    '- `line_dash_dot_setting`: LineDashDotSetting or None, default None',

    '  - A dash dot (1-dot chain) setting to set.':
    '  - 設定する一点鎖線のスタイル設定。',

    '- `parent`: ChildInterface or None, default None':
    '- `parent`: ChildInterface or None, default None',

    '  - A parent instance to add this instance. If a specified value is None, this interface uses a stage instance.':  # noqa
    '  - このインスタンスを追加する親のインスタンス。もしもNoneが指定された場合、このインスタンスはステージのインスタンスへと追加されます。',  # noqa

    '- `variable_name_suffix`: str, default \'\'':
    '- `variable_name_suffix`: str, default \'\'',

    '  - A JavaScript variable name suffix string. This setting is sometimes useful for JavaScript\'s debugging.':  # noqa
    '  - JavaScript上の変数のサフィックスの設定です。この設定はJavaScriptのデバッグ時に役立つことがあります。',

    '<hr>':
    '<hr>',

    '**[Examples]**':
    '**[コードサンプル]**',

    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> line: ap.Line = ap.Line(\n...    start_point=ap.Point2D(x=50, y=50),\n...    end_point=ap.Point2D(x=150, y=50),\n...    line_color=\'#ffffff\',\n...    line_thickness=3)\n>>> line.line_color\nString(\'#ffffff\')\n\n>>> line.line_thickness\nInt(3)\n```':  # noqa
    '```py\n>>> import apysc as ap\n>>> stage: ap.Stage = ap.Stage()\n>>> line: ap.Line = ap.Line(\n...    start_point=ap.Point2D(x=50, y=50),\n...    end_point=ap.Point2D(x=150, y=50),\n...    line_color=\'#ffffff\',\n...    line_thickness=3)\n>>> line.line_color\nString(\'#ffffff\')\n\n>>> line.line_thickness\nInt(3)\n```',  # noqa

}
