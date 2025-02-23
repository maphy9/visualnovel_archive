import React from 'react'
import style from './style.module.css'

function Choice({ type, setType, ownType, label }) {
  return (
    <div
    className={`${type === ownType ? style.active : style.inactive} ${style.choice}`}
    onClick={ () => setType(ownType) }
    >
      {ownType} {label}
    </div>
  )
}

export default Choice