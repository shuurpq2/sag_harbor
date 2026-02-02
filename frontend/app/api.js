export const getBackendUrl = () => {
    if (typeof(window) !== 'undefined') {
        const hostname = window.location.hostname;
        const port = '8000';
        return `http://${hostname}:${port}`;
    }
    return `http://192.168.31.26:8000`
}