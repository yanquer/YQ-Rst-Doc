============================
一些遇到过的报错
============================

报错内容::

  error /Users/yanque/project/webstorm/electron-study/node_modules/electron: Command failed.
  Exit code: 1
  Command: node install.js
  Arguments:
  Directory: project/webstorm/electron-study/node_modules/electron
  Output:
  ReadError: The server aborted pending request

原因: electron 下载不会使用本地配置的 `registry` 镜像,
需要额外配置 `electron_mirror`::

  yarn config set electron_mirror https://npm.taobao.org/mirrors/electron/


