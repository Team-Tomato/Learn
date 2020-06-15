const {BrowserWindow,app}=require('electron');

const path=require('path');
const url=require('url');

let win;

function createWindow(){
    win=new BrowserWindow({
        width:440,
        height:425,
        resizable: false,
    });
    win.loadURL(url.format({
        pathname:path.join(__dirname,'index.html'),
        protocol:'file',
        slashes:true
    }));
    win.on('closed',()=>{
        win=null;
    });
    win.setMenu=false;
}

app.on('ready',createWindow);
app.on('browser-window-created',function(e,window) {
    window.setMenu(null);
});