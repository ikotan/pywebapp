<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>アワビ！</title>
    <link rel="stylesheet" href="https://cdn.rawgit.com/Chalarangelo/mini.css/v2.3.7/dist/mini-default.min.css">
    % setdefault('use_bokeh', False)
    % if use_bokeh:
      <link href="http://cdn.pydata.org/bokeh/release/bokeh-0.12.13.min.css" rel="stylesheet" type="text/css">
      <script src="http://cdn.pydata.org/bokeh/release/bokeh-0.12.13.min.js"></script>
      {{ !script }}
    % end
    <meta name="viewport" content="width=device-width, initial-scale=1">
  </head>
  <body>
    <header>
      <a herf="/" class="button">
        アワビの年齢推定アプリケーション
      </a>
    </header>
    {{ !base }}
  </body>
</html>
