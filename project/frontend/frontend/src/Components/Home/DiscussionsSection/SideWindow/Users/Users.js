import React from 'react'
import style from './style.module.css'
import User from './User/User'

function Users({ users }) {
  const elements = users.map((user, index) => <User key={index} username={user.username} image={user.image} role={user.role} ranking={index + 1} joined={user.joined} />)
  return (
    <div className={style.users}>{elements}</div>
  )
}

export default Users