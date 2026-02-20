import { useState } from 'react'
import IconButton from '@mui/material/IconButton'
import freeroomsLogoOpen from '../../assets/freeRoomsLogo.png'
import freeroomsLogoClosed from '../../assets/freeroomsDoorClosed.png'
import styles from './Navbar.module.css'

export default function Navbar() {
  const [doorOpen, setDoorOpen] = useState(true)
  const [activeView, setActiveView] = useState('grid')

  return (
    <nav className={styles.navbar}>
      <div className={styles.logo} onClick={() => setDoorOpen(prev => !prev)}>
        <img
          src={doorOpen ? freeroomsLogoOpen : freeroomsLogoClosed}
          alt="Freerooms logo"
          className={styles.logoImg}
        />
        <span className={styles.logoText}>Freerooms</span>
      </div>

      <div className={styles.actions}>
        <IconButton
          aria-label="Search"
          onClick={() => setActiveView('search')}
          className={`${styles.iconBtn} ${activeView === 'search' ? styles.iconBtnActive : ''}`}
        >
          <span className="material-icons">search</span>
        </IconButton>
        <IconButton
          aria-label="Grid View"
          onClick={() => setActiveView('grid')}
          className={`${styles.iconBtn} ${activeView === 'grid' ? styles.iconBtnActive : ''}`}
        >
          <span className="material-icons">grid_view</span>
        </IconButton>
        <IconButton
          aria-label="Map"
          onClick={() => setActiveView('map')}
          className={`${styles.iconBtn} ${activeView === 'map' ? styles.iconBtnActive : ''}`}
        >
          <span className="material-icons">map</span>
        </IconButton>
        <IconButton
          aria-label="Dark Mode"
          onClick={() => setActiveView('dark')}
          className={`${styles.iconBtn} ${activeView === 'dark' ? styles.iconBtnActive : ''}`}
        >
          <span className="material-icons">dark_mode</span>
        </IconButton>
      </div>
    </nav>
  )
}
