import { buildings } from '../buildings'
import BuildingCard from './BuildingCard'
import styles from './BuildingGrid.module.css'

export default function BuildingGrid() {
  return (
    <main className={styles.grid}>
      {buildings.map((building) => (
        <BuildingCard key={building.name} building={building} />
      ))}
    </main>
  )
}

