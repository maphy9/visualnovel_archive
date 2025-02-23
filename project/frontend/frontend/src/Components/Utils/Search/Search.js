import React, { useEffect, useState } from 'react'
import style from './style.module.css'
import closeIcon from '../../../images/closeIcon.png'
import noImageIcon from '../../../images/noImageIcon.png'
import { SyncLoader } from 'react-spinners';
import Result from './Result/Result';

const fetchData = async (url, phrase, setData) => {
  const method = "POST";
  const headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
  };
  const body = JSON.stringify({ page_size: 5, page_number: 1, phrase });
  const res = await fetch(url, { method, headers, body });
  if (res.status !== 200) {
    console.error(`Error: ${res.status}`);
    return;
  }
  const data = await res.json();
  setData(data);
  console.dir(data);
};

function Search({ setIsSearchVisible }) {
  const [height, setHeight] = useState('');
  useEffect(() => {
    const updateHeight = () => {
      setHeight(`${document.documentElement.scrollHeight}px`);
    };
    updateHeight();
    window.addEventListener('resize', updateHeight);
    return () => window.removeEventListener('resize', updateHeight);
  }, []);

  const [phrase, setPhrase] = useState('');
  const handleChange = (e) => {
    const value = e.target.value;
    setPhrase(value);
  }

  const [visualNovels, setVisualNovels] = useState(null);
  useEffect(() => {
    fetchData('http://127.0.0.1:8000/find_visual_novels/', phrase, setVisualNovels);
  }, [phrase]);

  const [discussions, setDiscussions] = useState(null);
  useEffect(() => {
    fetchData('http://127.0.0.1:8000/find_discussions/', phrase, setDiscussions);
  }, [phrase]);

  const [users, setUsers] = useState(null);
  useEffect(() => {
    fetchData('http://127.0.0.1:8000/find_users/', phrase, setUsers);
  }, [phrase]);

  return (
    <>
      <div className={style.blurBackground} style={{ height }}></div>
      <div className={style.search}>
        <div className={style.close}><img onClick={ () => setIsSearchVisible(false) } src={closeIcon} alt="Close" /></div>
        <div className={style.search_bar}>
          <label htmlFor="phrase">Enter search phrase:</label>
          <br />
          <input onChange={handleChange} name="phrase" placeholder="Enter search phrase" />
        </div>
        <div className={style.results}>
          { visualNovels === null ? <SyncLoader color={"#70ACEB"} size={16} /> :
          visualNovels.length === 0 ? <></> :
          <>
            <h1>Visual novels</h1>
            {visualNovels.map((res, idx) => <Result title={res.title} image={res.image ? res.image : noImageIcon} key={idx} />)}
          </> }
        </div>
        <div className={style.results}>
          { discussions === null ? <SyncLoader color={"#70ACEB"} size={16} /> :
          discussions.length === 0 ? <></> :
          <>
            <h1>Discussions</h1>
            {discussions.map((res, idx) => <Result title={res.title} image={res.image ? res.image : noImageIcon} key={idx} />)}
          </> }
        </div>
        <div className={style.results}>
          { users === null ? <SyncLoader color={"#70ACEB"} size={16} /> :
          users.length === 0 ? <></> :
          <>
            <h1>Users</h1>
            {users.map((res, idx) => <Result title={res.title} image={res.image ? res.image : noImageIcon} key={idx} />)}
          </> }
        </div>
      </div>
    </>
  )
}

export default Search