const electron = require('electron')
const { app, BrowserWindow, Menu } = require('electron')

function createWindow () {
  // Create the browser window.
  const win = new BrowserWindow({
      title: "TT Calc",
    show: false,
    width:500,
    height: 320,
    maximizable: false,
    resizable: false,
    webPreferences: {
      nodeIntegration: true
    }
  })

  // and load the index.html of the app.
  win.loadFile('index.html')

  win.once('ready-to-show', () => {
    win.show()
  })

  // Open the DevTools.
  //win.webContents.openDevTools()
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.on('ready',function(){
  createWindow()

  const template = [
    {
        label: "File",
        submenu: [{ role: 'quit' }]
    },
    {
        label: "Help",
        submenu: [
          {label: 'About Team-Tomato',
          click: function(){
            electron.shell.openExternal('https://teamtomato.tech/#/')
          }
      }]
    }
];

  const menu = Menu.buildFromTemplate(template)
Menu.setApplicationMenu(menu)

})

// Quit when all windows are closed, except on macOS. There, it's common
// for applications and their menu bar to stay active until the user quits
// explicitly with Cmd + Q.
app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', () => {
  // On macOS it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow()
  }
})

// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and require them here.
