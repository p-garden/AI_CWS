{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/p-garden/AI_CWS/blob/main/src/rain.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "라이브러리 설정"
      ],
      "metadata": {
        "id": "fZR6Hm75OTyt"
      },
      "id": "fZR6Hm75OTyt"
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install import_ipynb\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "T1TPzBnue_Bm",
        "outputId": "7a313459-8674-47cd-8542-27ff4571c286"
      },
      "id": "T1TPzBnue_Bm",
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: import_ipynb in /usr/local/lib/python3.11/dist-packages (0.2)\n",
            "Requirement already satisfied: IPython in /usr/local/lib/python3.11/dist-packages (from import_ipynb) (7.34.0)\n",
            "Requirement already satisfied: nbformat in /usr/local/lib/python3.11/dist-packages (from import_ipynb) (5.10.4)\n",
            "Requirement already satisfied: setuptools>=18.5 in /usr/local/lib/python3.11/dist-packages (from IPython->import_ipynb) (75.1.0)\n",
            "Requirement already satisfied: jedi>=0.16 in /usr/local/lib/python3.11/dist-packages (from IPython->import_ipynb) (0.19.2)\n",
            "Requirement already satisfied: decorator in /usr/local/lib/python3.11/dist-packages (from IPython->import_ipynb) (4.4.2)\n",
            "Requirement already satisfied: pickleshare in /usr/local/lib/python3.11/dist-packages (from IPython->import_ipynb) (0.7.5)\n",
            "Requirement already satisfied: traitlets>=4.2 in /usr/local/lib/python3.11/dist-packages (from IPython->import_ipynb) (5.7.1)\n",
            "Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in /usr/local/lib/python3.11/dist-packages (from IPython->import_ipynb) (3.0.50)\n",
            "Requirement already satisfied: pygments in /usr/local/lib/python3.11/dist-packages (from IPython->import_ipynb) (2.18.0)\n",
            "Requirement already satisfied: backcall in /usr/local/lib/python3.11/dist-packages (from IPython->import_ipynb) (0.2.0)\n",
            "Requirement already satisfied: matplotlib-inline in /usr/local/lib/python3.11/dist-packages (from IPython->import_ipynb) (0.1.7)\n",
            "Requirement already satisfied: pexpect>4.3 in /usr/local/lib/python3.11/dist-packages (from IPython->import_ipynb) (4.9.0)\n",
            "Requirement already satisfied: fastjsonschema>=2.15 in /usr/local/lib/python3.11/dist-packages (from nbformat->import_ipynb) (2.21.1)\n",
            "Requirement already satisfied: jsonschema>=2.6 in /usr/local/lib/python3.11/dist-packages (from nbformat->import_ipynb) (4.23.0)\n",
            "Requirement already satisfied: jupyter-core!=5.0.*,>=4.12 in /usr/local/lib/python3.11/dist-packages (from nbformat->import_ipynb) (5.7.2)\n",
            "Requirement already satisfied: parso<0.9.0,>=0.8.4 in /usr/local/lib/python3.11/dist-packages (from jedi>=0.16->IPython->import_ipynb) (0.8.4)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=2.6->nbformat->import_ipynb) (25.1.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=2.6->nbformat->import_ipynb) (2024.10.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=2.6->nbformat->import_ipynb) (0.36.2)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=2.6->nbformat->import_ipynb) (0.22.3)\n",
            "Requirement already satisfied: platformdirs>=2.5 in /usr/local/lib/python3.11/dist-packages (from jupyter-core!=5.0.*,>=4.12->nbformat->import_ipynb) (4.3.6)\n",
            "Requirement already satisfied: ptyprocess>=0.5 in /usr/local/lib/python3.11/dist-packages (from pexpect>4.3->IPython->import_ipynb) (0.7.0)\n",
            "Requirement already satisfied: wcwidth in /usr/local/lib/python3.11/dist-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->IPython->import_ipynb) (0.2.13)\n",
            "Requirement already satisfied: typing-extensions>=4.4.0 in /usr/local/lib/python3.11/dist-packages (from referencing>=0.28.4->jsonschema>=2.6->nbformat->import_ipynb) (4.12.2)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install nbimporter"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oyiTY_1VkT-f",
        "outputId": "088e379c-c48c-455c-b2a6-1a70f9f6afa5"
      },
      "id": "oyiTY_1VkT-f",
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: nbimporter in /usr/local/lib/python3.11/dist-packages (0.3.4)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install datasets"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qgzRlmPyfLd9",
        "outputId": "082d2166-7001-410a-f8d2-f006015daeaf"
      },
      "id": "qgzRlmPyfLd9",
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting datasets\n",
            "  Downloading datasets-3.2.0-py3-none-any.whl.metadata (20 kB)\n",
            "Requirement already satisfied: filelock in /usr/local/lib/python3.11/dist-packages (from datasets) (3.17.0)\n",
            "Requirement already satisfied: numpy>=1.17 in /usr/local/lib/python3.11/dist-packages (from datasets) (1.26.4)\n",
            "Requirement already satisfied: pyarrow>=15.0.0 in /usr/local/lib/python3.11/dist-packages (from datasets) (17.0.0)\n",
            "Collecting dill<0.3.9,>=0.3.0 (from datasets)\n",
            "  Downloading dill-0.3.8-py3-none-any.whl.metadata (10 kB)\n",
            "Requirement already satisfied: pandas in /usr/local/lib/python3.11/dist-packages (from datasets) (2.2.2)\n",
            "Requirement already satisfied: requests>=2.32.2 in /usr/local/lib/python3.11/dist-packages (from datasets) (2.32.3)\n",
            "Requirement already satisfied: tqdm>=4.66.3 in /usr/local/lib/python3.11/dist-packages (from datasets) (4.67.1)\n",
            "Collecting xxhash (from datasets)\n",
            "  Downloading xxhash-3.5.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (12 kB)\n",
            "Collecting multiprocess<0.70.17 (from datasets)\n",
            "  Downloading multiprocess-0.70.16-py311-none-any.whl.metadata (7.2 kB)\n",
            "Collecting fsspec<=2024.9.0,>=2023.1.0 (from fsspec[http]<=2024.9.0,>=2023.1.0->datasets)\n",
            "  Downloading fsspec-2024.9.0-py3-none-any.whl.metadata (11 kB)\n",
            "Requirement already satisfied: aiohttp in /usr/local/lib/python3.11/dist-packages (from datasets) (3.11.11)\n",
            "Requirement already satisfied: huggingface-hub>=0.23.0 in /usr/local/lib/python3.11/dist-packages (from datasets) (0.28.1)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.11/dist-packages (from datasets) (24.2)\n",
            "Requirement already satisfied: pyyaml>=5.1 in /usr/local/lib/python3.11/dist-packages (from datasets) (6.0.2)\n",
            "Requirement already satisfied: aiohappyeyeballs>=2.3.0 in /usr/local/lib/python3.11/dist-packages (from aiohttp->datasets) (2.4.4)\n",
            "Requirement already satisfied: aiosignal>=1.1.2 in /usr/local/lib/python3.11/dist-packages (from aiohttp->datasets) (1.3.2)\n",
            "Requirement already satisfied: attrs>=17.3.0 in /usr/local/lib/python3.11/dist-packages (from aiohttp->datasets) (25.1.0)\n",
            "Requirement already satisfied: frozenlist>=1.1.1 in /usr/local/lib/python3.11/dist-packages (from aiohttp->datasets) (1.5.0)\n",
            "Requirement already satisfied: multidict<7.0,>=4.5 in /usr/local/lib/python3.11/dist-packages (from aiohttp->datasets) (6.1.0)\n",
            "Requirement already satisfied: propcache>=0.2.0 in /usr/local/lib/python3.11/dist-packages (from aiohttp->datasets) (0.2.1)\n",
            "Requirement already satisfied: yarl<2.0,>=1.17.0 in /usr/local/lib/python3.11/dist-packages (from aiohttp->datasets) (1.18.3)\n",
            "Requirement already satisfied: typing-extensions>=3.7.4.3 in /usr/local/lib/python3.11/dist-packages (from huggingface-hub>=0.23.0->datasets) (4.12.2)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests>=2.32.2->datasets) (3.4.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests>=2.32.2->datasets) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests>=2.32.2->datasets) (2.3.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests>=2.32.2->datasets) (2025.1.31)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.11/dist-packages (from pandas->datasets) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.11/dist-packages (from pandas->datasets) (2025.1)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.11/dist-packages (from pandas->datasets) (2025.1)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.11/dist-packages (from python-dateutil>=2.8.2->pandas->datasets) (1.17.0)\n",
            "Downloading datasets-3.2.0-py3-none-any.whl (480 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m480.6/480.6 kB\u001b[0m \u001b[31m8.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading dill-0.3.8-py3-none-any.whl (116 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m116.3/116.3 kB\u001b[0m \u001b[31m9.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading fsspec-2024.9.0-py3-none-any.whl (179 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m179.3/179.3 kB\u001b[0m \u001b[31m15.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading multiprocess-0.70.16-py311-none-any.whl (143 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m143.5/143.5 kB\u001b[0m \u001b[31m11.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading xxhash-3.5.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (194 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m194.8/194.8 kB\u001b[0m \u001b[31m16.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: xxhash, fsspec, dill, multiprocess, datasets\n",
            "  Attempting uninstall: fsspec\n",
            "    Found existing installation: fsspec 2024.10.0\n",
            "    Uninstalling fsspec-2024.10.0:\n",
            "      Successfully uninstalled fsspec-2024.10.0\n",
            "\u001b[31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.\n",
            "gcsfs 2024.10.0 requires fsspec==2024.10.0, but you have fsspec 2024.9.0 which is incompatible.\n",
            "torch 2.5.1+cu124 requires nvidia-cublas-cu12==12.4.5.8; platform_system == \"Linux\" and platform_machine == \"x86_64\", but you have nvidia-cublas-cu12 12.5.3.2 which is incompatible.\n",
            "torch 2.5.1+cu124 requires nvidia-cuda-cupti-cu12==12.4.127; platform_system == \"Linux\" and platform_machine == \"x86_64\", but you have nvidia-cuda-cupti-cu12 12.5.82 which is incompatible.\n",
            "torch 2.5.1+cu124 requires nvidia-cuda-nvrtc-cu12==12.4.127; platform_system == \"Linux\" and platform_machine == \"x86_64\", but you have nvidia-cuda-nvrtc-cu12 12.5.82 which is incompatible.\n",
            "torch 2.5.1+cu124 requires nvidia-cuda-runtime-cu12==12.4.127; platform_system == \"Linux\" and platform_machine == \"x86_64\", but you have nvidia-cuda-runtime-cu12 12.5.82 which is incompatible.\n",
            "torch 2.5.1+cu124 requires nvidia-cudnn-cu12==9.1.0.70; platform_system == \"Linux\" and platform_machine == \"x86_64\", but you have nvidia-cudnn-cu12 9.3.0.75 which is incompatible.\n",
            "torch 2.5.1+cu124 requires nvidia-cufft-cu12==11.2.1.3; platform_system == \"Linux\" and platform_machine == \"x86_64\", but you have nvidia-cufft-cu12 11.2.3.61 which is incompatible.\n",
            "torch 2.5.1+cu124 requires nvidia-curand-cu12==10.3.5.147; platform_system == \"Linux\" and platform_machine == \"x86_64\", but you have nvidia-curand-cu12 10.3.6.82 which is incompatible.\n",
            "torch 2.5.1+cu124 requires nvidia-cusolver-cu12==11.6.1.9; platform_system == \"Linux\" and platform_machine == \"x86_64\", but you have nvidia-cusolver-cu12 11.6.3.83 which is incompatible.\n",
            "torch 2.5.1+cu124 requires nvidia-cusparse-cu12==12.3.1.170; platform_system == \"Linux\" and platform_machine == \"x86_64\", but you have nvidia-cusparse-cu12 12.5.1.3 which is incompatible.\n",
            "torch 2.5.1+cu124 requires nvidia-nvjitlink-cu12==12.4.127; platform_system == \"Linux\" and platform_machine == \"x86_64\", but you have nvidia-nvjitlink-cu12 12.5.82 which is incompatible.\u001b[0m\u001b[31m\n",
            "\u001b[0mSuccessfully installed datasets-3.2.0 dill-0.3.8 fsspec-2024.9.0 multiprocess-0.70.16 xxhash-3.5.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vSrW4wpyMiEV",
        "outputId": "1ad922ed-f6b7-42b4-ad67-6ac589c845e9"
      },
      "id": "vSrW4wpyMiEV",
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount(\"/content/drive\", force_remount=True).\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "id": "zu8kQt_7GTRf",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zu8kQt_7GTRf",
        "outputId": "e82a8ee2-23ef-4928-8b40-4a3ef375ba9f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/drive/MyDrive/BITAMIN/gen_question/requirements.txt\n",
            "Collecting cudf-cu12@ https://pypi.nvidia.com/cudf-cu12/cudf_cu12-24.12.0-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (from -r /content/drive/MyDrive/BITAMIN/gen_question/requirements.txt (line 62))\n",
            "  Downloading https://pypi.nvidia.com/cudf-cu12/cudf_cu12-24.12.0-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (26.9 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m26.9/26.9 MB\u001b[0m \u001b[31m182.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting en-core-web-sm@ https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.7.1/en_core_web_sm-3.7.1-py3-none-any.whl#sha256=86cc141f63942d4b2c5fcee06630fd6f904788d2f0ab005cce45aadb8fb73889 (from -r /content/drive/MyDrive/BITAMIN/gen_question/requirements.txt (line 95))\n",
            "  Downloading https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.7.1/en_core_web_sm-3.7.1-py3-none-any.whl (12.8 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m12.8/12.8 MB\u001b[0m \u001b[31m37.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hProcessing /colabtools/dist/google_colab-1.0.0.tar.gz (from -r /content/drive/MyDrive/BITAMIN/gen_question/requirements.txt (line 155))\n",
            "\u001b[31mERROR: Could not install packages due to an OSError: [Errno 2] No such file or directory: '/colabtools/dist/google_colab-1.0.0.tar.gz'\n",
            "\u001b[0m\u001b[31m\n",
            "\u001b[0m"
          ]
        }
      ],
      "source": [
        "!ls /content/drive/MyDrive/BITAMIN/gen_question/requirements.txt\n",
        "!pip install -r /content/drive/MyDrive/BITAMIN/gen_question/requirements.txt"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%cd /content/drive/MyDrive/BITAMIN/gen_question/src"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BHveDQq8St2E",
        "outputId": "21bfcbcb-59a1-4814-a735-50563c2c6f12"
      },
      "id": "BHveDQq8St2E",
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/drive/MyDrive/BITAMIN/gen_question/src\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "id": "8edfa330-00b3-46d6-af06-cb095cd83e10",
      "metadata": {
        "id": "8edfa330-00b3-46d6-af06-cb095cd83e10"
      },
      "outputs": [],
      "source": [
        "def preprocess_function(examples):\n",
        "    model_inputs = tokenizer(\n",
        "        examples[\"input_text\"],\n",
        "        max_length=512,\n",
        "        padding=\"max_length\",\n",
        "        truncation=True\n",
        "    )\n",
        "\n",
        "    labels = tokenizer(\n",
        "        examples[\"target_text\"],\n",
        "        max_length=128,\n",
        "        padding=\"max_length\",\n",
        "        truncation=True\n",
        "    )\n",
        "\n",
        "    model_inputs[\"labels\"] = labels[\"input_ids\"]\n",
        "    return model_inputs"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "f3ec6db6-ff4d-44fe-ae89-6a415628d9de",
      "metadata": {
        "id": "f3ec6db6-ff4d-44fe-ae89-6a415628d9de",
        "outputId": "994119e8-67a9-4903-b23a-e0d9aa94975e"
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "You passed along `num_labels=3` with an incompatible id to label map: {'0': 'NEGATIVE', '1': 'POSITIVE'}. The number of labels wil be overwritten to 2.\n"
          ]
        },
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "\n",
            "✅ 변환된 Train Dataset 샘플:\n",
            "{'input_text': '정답: 교향곡 문맥: 1839년 바그너는 괴테의 파우스트을 처음 읽고 그 내용에 마음이 끌려 이를 소재로 해서 하나의 교향곡을 쓰려는 뜻을 갖는다. 이 시기 바그너는 1838년에 빛 독촉으로 산전수전을 다 걲은 상황이라 좌절과 실망에 가득했으며 메피스토펠레스를 만나는 파우스트의 심경에 공감했다고 한다. 또한 파리에서 아브네크의 지휘로 파리 음악원 관현악단이 연주하는 베토벤의 교향곡 9번을 듣고 깊은 감명을 받았는데, 이것이 이듬해 1월에 파우스트의 서곡으로 쓰여진 이 작품에 조금이라도 영향을 끼쳤으리라는 것은 의심할 여지가 없다. 여기의 라단조 조성의 경우에도 그의 전기에 적혀 있는 것처럼 단순한 정신적 피로나 실의가 반영된 것이 아니라 베토벤의 합창교향곡 조성의 영향을 받은 것을 볼 수 있다. 그렇게 교향곡 작곡을 1839년부터 40년에 걸쳐 파리에서 착수했으나 1악장을 쓴 뒤에 중단했다. 또한 작품의 완성과 동시에 그는 이 서곡(1악장)을 파리 음악원의 연주회에서 연주할 파트보까지 준비하였으나, 실제로는 이루어지지는 않았다. 결국 초연은 4년 반이 지난 후에 드레스덴에서 연주되었고 재연도 이루어졌지만, 이후에 그대로 방치되고 말았다. 그 사이에 그는 리엔치와 방황하는 네덜란드인을 완성하고 탄호이저에도 착수하는 등 분주한 시간을 보냈는데, 그런 바쁜 생활이 이 곡을 잊게 한 것이 아닌가 하는 의견도 있다.', 'target_text': '바그너는 괴테의 파우스트를 읽고 무엇을 쓰고자 했는가?'}\n",
            "{'input_text': '정답: 1악장 문맥: 1839년 바그너는 괴테의 파우스트을 처음 읽고 그 내용에 마음이 끌려 이를 소재로 해서 하나의 교향곡을 쓰려는 뜻을 갖는다. 이 시기 바그너는 1838년에 빛 독촉으로 산전수전을 다 걲은 상황이라 좌절과 실망에 가득했으며 메피스토펠레스를 만나는 파우스트의 심경에 공감했다고 한다. 또한 파리에서 아브네크의 지휘로 파리 음악원 관현악단이 연주하는 베토벤의 교향곡 9번을 듣고 깊은 감명을 받았는데, 이것이 이듬해 1월에 파우스트의 서곡으로 쓰여진 이 작품에 조금이라도 영향을 끼쳤으리라는 것은 의심할 여지가 없다. 여기의 라단조 조성의 경우에도 그의 전기에 적혀 있는 것처럼 단순한 정신적 피로나 실의가 반영된 것이 아니라 베토벤의 합창교향곡 조성의 영향을 받은 것을 볼 수 있다. 그렇게 교향곡 작곡을 1839년부터 40년에 걸쳐 파리에서 착수했으나 1악장을 쓴 뒤에 중단했다. 또한 작품의 완성과 동시에 그는 이 서곡(1악장)을 파리 음악원의 연주회에서 연주할 파트보까지 준비하였으나, 실제로는 이루어지지는 않았다. 결국 초연은 4년 반이 지난 후에 드레스덴에서 연주되었고 재연도 이루어졌지만, 이후에 그대로 방치되고 말았다. 그 사이에 그는 리엔치와 방황하는 네덜란드인을 완성하고 탄호이저에도 착수하는 등 분주한 시간을 보냈는데, 그런 바쁜 생활이 이 곡을 잊게 한 것이 아닌가 하는 의견도 있다.', 'target_text': '바그너는 교향곡 작곡을 어디까지 쓴 뒤에 중단했는가?'}\n",
            "✅ 학습 데이터 개수: 800개\n",
            "✅ 검증 데이터 개수: 200개\n"
          ]
        },
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "Map: 100%|███████████████████████████████████████████████████████████████████| 800/800 [00:01<00:00, 672.83 examples/s]\n",
            "Map: 100%|██████████████████████████████████████████████████████████████████| 200/200 [00:00<00:00, 1123.62 examples/s]\n"
          ]
        }
      ],
      "source": [
        "from dataset import get_datasets\n",
        "from model import load_model\n",
        "from transformers import TrainingArguments, Trainer\n",
        "\n",
        "# 모델 및 데이터 로드\n",
        "tokenizer, model = load_model()\n",
        "train_dataset, valid_dataset = get_datasets()  #  `dataset.py`에서 변환된 데이터 가져오기\n",
        "\n",
        "TRAIN_SAMPLE_SIZE = 800  # 학습 데이터 샘플 개수\n",
        "VALID_SAMPLE_SIZE = 200  # 검증 데이터 샘플 개수\n",
        "\n",
        "train_dataset = train_dataset.shuffle(seed=42).select(range(min(len(train_dataset), TRAIN_SAMPLE_SIZE)))\n",
        "valid_dataset = valid_dataset.shuffle(seed=42).select(range(min(len(valid_dataset), VALID_SAMPLE_SIZE)))\n",
        "\n",
        "print(f\"✅ 학습 데이터 개수: {len(train_dataset)}개\")\n",
        "print(f\"✅ 검증 데이터 개수: {len(valid_dataset)}개\")\n",
        "\n",
        "# 데이터 전처리 preprocess 함수 사용\n",
        "train_tokenized = train_dataset.map(preprocess_function, batched=True)\n",
        "valid_tokenized = valid_dataset.map(preprocess_function, batched=True)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 25,
      "id": "df9d2402-e4bf-4fdb-bd20-6a2a5d1f3d6a",
      "metadata": {
        "id": "df9d2402-e4bf-4fdb-bd20-6a2a5d1f3d6a",
        "outputId": "f03ecfab-2176-4fae-9157-90754bbc1d80",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 224
        }
      },
      "outputs": [
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "name 'TrainingArguments' is not defined",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-25-1f59095d41a2>\u001b[0m in \u001b[0;36m<cell line: 2>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m# ✅ 학습 파라미터 설정\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m training_args = TrainingArguments(\n\u001b[0m\u001b[1;32m      3\u001b[0m     \u001b[0moutput_dir\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"../saved_model/kobart_qg_finetuned\"\u001b[0m\u001b[0;34m,\u001b[0m  \u001b[0;31m# 모델 저장 경로\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m     \u001b[0mevaluation_strategy\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"steps\"\u001b[0m\u001b[0;34m,\u001b[0m    \u001b[0;31m# 평가를 steps마다 실행\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m     \u001b[0msave_strategy\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"steps\"\u001b[0m\u001b[0;34m,\u001b[0m          \u001b[0;31m# 모델 저장도 steps마다 실|행\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mNameError\u001b[0m: name 'TrainingArguments' is not defined"
          ]
        }
      ],
      "source": [
        "# ✅ 학습 파라미터 설정\n",
        "training_args = TrainingArguments(\n",
        "    output_dir=\"../saved_model/kobart_qg_finetuned\",  # 모델 저장 경로\n",
        "    evaluation_strategy=\"steps\",    # 평가를 steps마다 실행\n",
        "    save_strategy=\"steps\",          # 모델 저장도 steps마다 실|행\n",
        "    save_steps=500,                 # 500 스텝마다 저장\n",
        "    eval_steps=500,                 # 500 스텝마다 평가\n",
        "    learning_rate=3e-5,\n",
        "    per_device_train_batch_size=8,\n",
        "    per_device_eval_batch_size=8,\n",
        "    num_train_epochs=3,\n",
        "    weight_decay=0.01,\n",
        "    save_total_limit=2,\n",
        "    logging_dir=\"./logs\",\n",
        "    logging_steps=100,\n",
        "    load_best_model_at_end=True,    # 최적 모델 로드\n",
        ")\n",
        "\n",
        "# ✅ Trainer 객체 생성\n",
        "trainer = Trainer(\n",
        "    model=model,\n",
        "    args=training_args,\n",
        "    train_dataset=train_tokenized,\n",
        "    eval_dataset=valid_tokenized,\n",
        "    tokenizer=tokenizer,\n",
        ")\n",
        "\n",
        "# ✅ 학습 실행\n",
        "if __name__ == \"__main__\":\n",
        "    print(\"🚀 모델 학습 시작...\")\n",
        "    trainer.train()\n",
        "\n",
        "    # 학습된 모델 저장\n",
        "    model.save_pretrained(\"../saved_model/kobart_qg_finetuned\")\n",
        "    tokenizer.save_pretrained(\"../saved_model/kobart_qg_finetuned\")\n",
        "    print(\"✅ 모델 학습 완료 및 저장됨!\")"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "0db5d695-a4b0-45f4-b984-4a92917731db",
      "metadata": {
        "id": "0db5d695-a4b0-45f4-b984-4a92917731db"
      },
      "source": [
        "추가학습 코드 / 1000개 단위로 학습할 예정(random data)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 22,
      "id": "9204af0e-ff81-4148-a848-2d0a41cfe02f",
      "metadata": {
        "id": "9204af0e-ff81-4148-a848-2d0a41cfe02f",
        "outputId": "5d06eb98-6bf9-4433-e6d3-96e595af8195",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 471
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "You passed along `num_labels=3` with an incompatible id to label map: {'0': 'NEGATIVE', '1': 'POSITIVE'}. The number of labels wil be overwritten to 2.\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "✅ 추가 학습 데이터 개수: 10개\n",
            "✅ 검증 데이터 개수: 2개\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.11/dist-packages/transformers/training_args.py:1575: FutureWarning: `evaluation_strategy` is deprecated and will be removed in version 4.46 of 🤗 Transformers. Use `eval_strategy` instead\n",
            "  warnings.warn(\n",
            "<ipython-input-22-272affbc3020>:52: FutureWarning: `tokenizer` is deprecated and will be removed in version 5.0.0 for `Trainer.__init__`. Use `processing_class` instead.\n",
            "  trainer = Trainer(\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "🚀 추가 학습 시작...\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "    <div>\n",
              "      \n",
              "      <progress value='6' max='6' style='width:300px; height:20px; vertical-align: middle;'></progress>\n",
              "      [6/6 00:08, Epoch 3/3]\n",
              "    </div>\n",
              "    <table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              " <tr style=\"text-align: left;\">\n",
              "      <th>Step</th>\n",
              "      <th>Training Loss</th>\n",
              "      <th>Validation Loss</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <td>1</td>\n",
              "      <td>0.003900</td>\n",
              "      <td>0.667213</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td>2</td>\n",
              "      <td>0.026600</td>\n",
              "      <td>0.668054</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td>3</td>\n",
              "      <td>0.017000</td>\n",
              "      <td>0.666433</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td>4</td>\n",
              "      <td>0.003200</td>\n",
              "      <td>0.665672</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td>5</td>\n",
              "      <td>0.004000</td>\n",
              "      <td>0.665041</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <td>6</td>\n",
              "      <td>0.006400</td>\n",
              "      <td>0.665056</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table><p>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "Could not locate the best model at ../saved_model/kobart_qg_finetuned/checkpoint-5/pytorch_model.bin, if you are running a distributed training on multiple nodes, you should activate `--save_on_each_node`.\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "✅ 추가 학습 완료 및 저장됨!\n"
          ]
        }
      ],
      "source": [
        "import import_ipynb\n",
        "import nbimporter\n",
        "\n",
        "from dataset import get_datasets\n",
        "from model import load_model\n",
        "from transformers import TrainingArguments, Trainer\n",
        "import torch\n",
        "import os\n",
        "\n",
        "\n",
        "# ✅ 기존 학습된 모델 로드 (추가 학습)\n",
        "MODEL_PATH = \"../saved_model/kobart_qg_finetuned\"  # 이전 학습된 모델 경로\n",
        "tokenizer, model = load_model(MODEL_PATH)  # 기존 모델 불러오기\n",
        "train_dataset, valid_dataset = get_datasets()  # 새로운 데이터셋 로드\n",
        "\n",
        "# ✅ 추가 학습 시 데이터 일부만 사용 (샘플링)\n",
        "TRAIN_SAMPLE_SIZE = 10  # 학습 데이터 샘플 개수\n",
        "VALID_SAMPLE_SIZE = 2 # 검증 데이터 샘플 개수\n",
        "\n",
        "train_dataset = train_dataset.shuffle().select(range(min(len(train_dataset), TRAIN_SAMPLE_SIZE)))\n",
        "valid_dataset = valid_dataset.shuffle().select(range(min(len(valid_dataset), VALID_SAMPLE_SIZE)))\n",
        "\n",
        "print(f\"✅ 추가 학습 데이터 개수: {len(train_dataset)}개\")\n",
        "print(f\"✅ 검증 데이터 개수: {len(valid_dataset)}개\")\n",
        "\n",
        "train_tokenized = train_dataset.map(preprocess_function, batched=True)\n",
        "valid_tokenized = valid_dataset.map(preprocess_function, batched=True)\n",
        "\n",
        "# ✅ 추가 학습을 위한 TrainingArguments 설정\n",
        "training_args = TrainingArguments(\n",
        "    output_dir=\"../saved_model/kobart_qg_finetuned\",  # 새로운 모델 저장 경로\n",
        "    evaluation_strategy=\"steps\",  # 매 steps마다 평가\n",
        "    save_strategy=\"steps\",          # 모델 저장도 steps마다 실|행\n",
        "    learning_rate=3e-5,\n",
        "    logging_steps=1,\n",
        "    disable_tqdm=False,\n",
        "    per_device_train_batch_size=8,\n",
        "    per_device_eval_batch_size=8,\n",
        "    num_train_epochs=3,  # 추가 학습 3 Epoch\n",
        "    save_steps=300,  # 300 스텝마다 모델 저장\n",
        "    save_total_limit=2,  # 최신 모델 2개만 저장\n",
        "    logging_dir=\"../logs\",\n",
        "    #logging_steps=100,  # 100 스텝마다 로그 출력\n",
        "    load_best_model_at_end=True,  # 가장 좋은 모델 불러오기\n",
        "    metric_for_best_model=\"eval_loss\",\n",
        "    resume_from_checkpoint=True,  # ✅ 기존 체크포인트에서 이어서 학습\n",
        "    report_to=\"none\"  # wandb 로그 사용 안 함\n",
        "\n",
        ")\n",
        "\n",
        "# ✅ Trainer 객체 생성\n",
        "trainer = Trainer(\n",
        "    model=model,\n",
        "    args=training_args,\n",
        "    train_dataset=train_tokenized,\n",
        "    eval_dataset=valid_tokenized,\n",
        "    tokenizer=tokenizer,\n",
        ")\n",
        "os.environ[\"WANDB_DISABLED\"] = \"true\"\n",
        "\n",
        "\n",
        "# ✅ 학습 실행\n",
        "if __name__ == \"__main__\":\n",
        "    print(\"🚀 추가 학습 시작...\")\n",
        "    trainer.train()\n",
        "\n",
        "    # 학습된 모델 저장\n",
        "    model.save_pretrained(\"../saved_model/kobart_qg_finetuned\", torch_dtype=torch.float16, safe_serialization=False)\n",
        "    tokenizer.save_pretrained(\"../saved_model/kobart_qg_finetuned\")\n",
        "    print(\"✅ 추가 학습 완료 및 저장됨!\")\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "id": "1f75b850-f8fe-4f73-9bfe-ebc79abef2c6",
      "metadata": {
        "id": "1f75b850-f8fe-4f73-9bfe-ebc79abef2c6",
        "outputId": "5dc9f8e3-f751-4ebd-b307-e36858aeb6c8"
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "You passed along `num_labels=3` with an incompatible id to label map: {'0': 'NEGATIVE', '1': 'POSITIVE'}. The number of labels wil be overwritten to 2.\n"
          ]
        },
        {
          "data": {
            "text/plain": [
              "('../saved_model/kobart_qg_finetuned\\\\tokenizer_config.json',\n",
              " '../saved_model/kobart_qg_finetuned\\\\special_tokens_map.json',\n",
              " '../saved_model/kobart_qg_finetuned\\\\tokenizer.json')"
            ]
          },
          "execution_count": 8,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "# ✅ 최신 체크포인트 경로 설정 (예: checkpoint-1500)\n",
        "CHECKPOINT_PATH = \"../saved_model/kobart_qg_finetuned/checkpoint-900\"\n",
        "\n",
        "# ✅ 모델 & 토크나이저 로드\n",
        "tokenizer, model = load_model(CHECKPOINT_PATH)\n",
        "\n",
        "model.save_pretrained(\"../saved_model/kobart_qg_finetuned\", torch_dtype=torch.float16, safe_serialization=False)\n",
        "tokenizer.save_pretrained(\"../saved_model/kobart_qg_finetuned\")\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip freeze > ../requirements.txt\n"
      ],
      "metadata": {
        "id": "spP0XzRaaZM0"
      },
      "id": "spP0XzRaaZM0",
      "execution_count": 22,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install --upgrade protobuf\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0GeN6BlyaZiF",
        "outputId": "5c7767a4-d4be-4940-bd37-085d1a1c841f"
      },
      "id": "0GeN6BlyaZiF",
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: protobuf in /usr/local/lib/python3.11/dist-packages (5.29.3)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import glob\n",
        "import os\n",
        "\n",
        "notebooks = glob.glob(\"*.ipynb\")  # 현재 디렉토리의 모든 .ipynb 파일 찾기\n",
        "\n",
        "for notebook in notebooks:\n",
        "    py_file = notebook.replace(\".ipynb\", \".py\")\n",
        "    !jupyter nbconvert --to script {notebook}\n",
        "    print(f\"✅ {py_file} 변환 완료!\")\n",
        "\n",
        "# 변환된 파일을 Google Drive에 저장\n",
        "drive_path = \"/content/drive/MyDrive/BITAMIN/gen_question/src/\"\n",
        "os.makedirs(drive_path, exist_ok=True)\n",
        "!mv *.py {drive_path}\n",
        "\n",
        "print(f\"📂 모든 .py 파일이 {drive_path}에 저장되었습니다!\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZyDpP26mloAU",
        "outputId": "d7978acb-6d06-4073-fd4e-3a9cee2f701b"
      },
      "id": "ZyDpP26mloAU",
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[NbConvertApp] Converting notebook KOBART_GQ.ipynb to script\n",
            "[NbConvertApp] Writing 9323 bytes to KOBART_GQ.py\n",
            "✅ KOBART_GQ.py 변환 완료!\n",
            "[NbConvertApp] Converting notebook infer.ipynb to script\n",
            "[NbConvertApp] Writing 5342 bytes to infer.py\n",
            "✅ infer.py 변환 완료!\n",
            "[NbConvertApp] Converting notebook model.ipynb to script\n",
            "[NbConvertApp] Writing 7170 bytes to model.py\n",
            "✅ model.py 변환 완료!\n",
            "[NbConvertApp] Converting notebook dataset.ipynb to script\n",
            "[NbConvertApp] Writing 1988 bytes to dataset.py\n",
            "✅ dataset.py 변환 완료!\n",
            "[NbConvertApp] Converting notebook train.ipynb to script\n",
            "[NbConvertApp] Writing 5642 bytes to train.txt\n",
            "✅ train.py 변환 완료!\n",
            "mv: 'dataset.py' and '/content/drive/MyDrive/BITAMIN/gen_question/src/dataset.py' are the same file\n",
            "mv: 'infer.py' and '/content/drive/MyDrive/BITAMIN/gen_question/src/infer.py' are the same file\n",
            "mv: '__init__.py' and '/content/drive/MyDrive/BITAMIN/gen_question/src/__init__.py' are the same file\n",
            "mv: 'KOBART_GQ.py' and '/content/drive/MyDrive/BITAMIN/gen_question/src/KOBART_GQ.py' are the same file\n",
            "mv: 'model.py' and '/content/drive/MyDrive/BITAMIN/gen_question/src/model.py' are the same file\n",
            "mv: 'train.py' and '/content/drive/MyDrive/BITAMIN/gen_question/src/train.py' are the same file\n",
            "📂 모든 .py 파일이 /content/drive/MyDrive/BITAMIN/gen_question/src/에 저장되었습니다!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "owvNw5b_rYfp"
      },
      "id": "owvNw5b_rYfp",
      "execution_count": null,
      "outputs": []
    }
  ],
  "metadata": {
    "accelerator": "GPU",
    "colab": {
      "gpuType": "T4",
      "provenance": [],
      "include_colab_link": true
    },
    "jupytext": {
      "formats": "ipynb,py:light"
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 5
}