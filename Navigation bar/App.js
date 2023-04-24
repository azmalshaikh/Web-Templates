import { useState } from 'react';
import './App.css';
import Header from './components/header/Header.js';
import Sidebar from './components/sidebar'
import FilesView from './components/filesView/FilesView'
import SideIcons from './components/sideIcons'
import { auth, provider } from "./firebase";
import GDriveLogo from "./media/logo.png";

function App() {

  // const [user, setUser] = useState()
  // const [user, setUser] = useState({
  //   displayName: "Azmal Shaikh",
  //   email: "azmalshaikh59@gmail.com",
  //   emailVerified: true,
  //   phoneNumber: null,
  //   photoURL: "https://lh6.googleusercontent.com/-KyLTWqvDIHQ/AAAAAAAAAAI/AAAAAAAAAAA/AMZuuclcWGWqkt6YUAan32YO4CSR07Y2jw/s96-c/photo.jpg"
  // })

  const handleLogin = () => {
    if (!user) {
      auth.signInWithPopup(provider).then((result) => {
        setUser(result.user)
        console.log(result.user)
      }).catch((error) => {
        alert(error.message);
      });
    }
  }

  // Authentication

  return (
    <div className="app">
      {
        user ? (
          <>
            <Header userPhoto={user.photoURL} setUser={setUser}/>
            <div className="app__main">
              <Sidebar user={user.email}/>
              <FilesView user={user.email}/>
              <SideIcons />
            </div>
          </>
        ) : (
            <div className='app__login'>
              <img src={GDriveLogo} alt="Google Drive" className="app__loginImage"/>
              <p className="app__loginHeading">Google Drive Clone</p>
              <button onClick={handleLogin}>Log in to Google Drive</button>
            </div>
          )
      }
    </div>
  );
}

export default App;
