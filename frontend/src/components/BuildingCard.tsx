import { Building } from '../buildings'
import styles from './BuildingCard.module.css'

interface BuildingCardProps {
  building: Building
}

export default function BuildingCard({ building }: BuildingCardProps) {
  const { name, rooms_available, image } = building

  return (
    <div className={styles.card}>
      <img src={image} alt={name} className={styles.image} />

      <div className={styles.badge}>
        <span className={styles.dot} />
        <span className={styles.badgeDesktop}>{rooms_available} rooms available</span>
        <span className={styles.badgeMobile}>{rooms_available}/{rooms_available}</span>
      </div>

      <div className={styles.nameLabel}>
        {name}
      </div>
    </div>
  )
}

