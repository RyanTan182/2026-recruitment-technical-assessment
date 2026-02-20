import dataJson from '../data.json'

import agsm from '../assets/agsm.webp'
import ainsworth from '../assets/ainsworth.webp'
import anitab from '../assets/anitab.webp'
import biologicalScience from '../assets/biologicalScience.webp'
import biologicalScienceWest from '../assets/biologicalScienceWest.webp'
import blockhouse from '../assets/blockhouse.webp'
import businessSchool from '../assets/businessSchool.webp'
import civilBuilding from '../assets/civilBuilding.webp'
import colombo from '../assets/colombo.webp'
import cseBuilding from '../assets/cseBuilding.webp'

const imageMap: Record<string, string> = {
  'agsm.webp': agsm,
  'ainsworth.webp': ainsworth,
  'anitab.webp': anitab,
  'biologicalScience.webp': biologicalScience,
  'biologicalScienceWest.webp': biologicalScienceWest,
  'blockhouse.webp': blockhouse,
  'businessSchool.webp': businessSchool,
  'civilBuilding.webp': civilBuilding,
  'colombo.webp': colombo,
  'cseBuilding.webp': cseBuilding,
}

export interface Building {
  name: string
  rooms_available: number
  image: string
}

// Normalise the raw JSON: handle both "building_file" and "building_picture"
// keys, and strip any leading "./" so the imageMap lookup is consistent.
export const buildings: Building[] = dataJson.map((entry) => {
  const rawPath =
    ('building_picture' in entry ? entry.building_picture : entry.building_file) ?? ''
  const filename = rawPath.replace(/^\.\//, '')
  return {
    name: entry.name,
    rooms_available: entry.rooms_available,
    image: imageMap[filename] ?? '',
  }
})
