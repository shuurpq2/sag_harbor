'use client'
import axios from 'axios';
import cl from './page.module.css'
import { getBackendUrl } from '../api';
import { useRef, useState } from 'react';
import Link from 'next/link';


export default function ImgConverter() {
  const [downloadUrl, setDownloadUrl] = useState('')
  const [downloadPath, setDownloadPath] = useState('')
  const imgRef = useRef()
  const formatRef = useRef()
  const API_URL = getBackendUrl()
  const convertImg = async() => {
    const formData = new FormData
    formData.append('uploaded_img', imgRef.current.files[0])
    const response = await axios.post(`${API_URL}/api/img_converter?format=${formatRef.current.value}`, formData, {responseType: 'blob'})
    const url = window.URL.createObjectURL(new Blob([response.data]))
    setDownloadUrl(url)
    const imgFormat = response.data.type.slice(response.data.type.indexOf('/') + 1)
    const imgName = imgRef.current.files[0].name
    setDownloadPath(`${imgName.slice(0, imgName.lastIndexOf('.'))}.${imgFormat}`)
  }
  return (
    <div className={cl.Content}>
      <input type='file' ref={imgRef} onChange={() => setDownloadUrl('')}/>
      <select ref={formatRef} onChange={() => setDownloadUrl('')}>
        <option>PNG</option>
        <option>JPG</option>
        <option>JPEG</option>
        <option>ICO</option>
      </select>
      <button onClick={() => convertImg()}>CONVERT</button>
      {downloadUrl && <Link href={downloadUrl} download={downloadPath}>DOWNLOAD</Link>}
    </div>
  );
}
