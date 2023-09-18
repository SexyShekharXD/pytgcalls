from typing import Dict
from typing import List
from typing import Optional

# TODO refactor needed
class FFprobe:
    @staticmethod
    def ffmpeg_headers(headers: Optional[Dict[str, str]] = None):
        ffmpeg_params: List[str] = []
        if headers is not None:
            ffmpeg_params.append('-headers')
            built_header = ''
            for key, value in headers.items():
                built_header += f'"{key}: {value}\\r\\n"'
            ffmpeg_params.append(built_header)
        return ' '.join(ffmpeg_params)
