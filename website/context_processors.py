"""
memo:

context_processors.py は、テンプレートに渡す変数を定義するファイルです。
settings.py の TEMPLATES の OPTIONS の context_processors に、このファイルを指定します。
context_processors.py には、関数を定義します。
関数の引数には、request が渡されます。
関数の戻り値には、テンプレートに渡す変数を辞書型で定義します。
"""


def common(request):
    var = 'pocari'
    return {"common_var": var}
