const {remote} = require('electron');

document.getElementById('close').addEventListener('click', closeWindow);
document.getElementById('minimize').addEventListener('click', minimizeWindow);
document.getElementById('maximize').addEventListener('click', maximizeWindow);

function closeWindow () {
    var window = remote.BrowserWindow.getFocusedWindow();
    window.close();
}

function minimizeWindow () {  
    var window = remote.BrowserWindow.getFocusedWindow();
    window.minimize();
}

function maximizeWindow () {
    var window = remote.BrowserWindow.getFocusedWindow();
    window.setFullScreen(!window.isFullScreen());
  }

