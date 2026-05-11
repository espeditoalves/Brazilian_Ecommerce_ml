import shutil
from pathlib import Path

import kagglehub


def clear_kagglehub_datasets_cache(cache_dir: str | Path) -> None:
    """
    Recebe um caminho interno do cache do kagglehub e encontra a pasta
    'datasets' para removê-la completamente.

    Exemplo:
    cache_dir:
    C:/Users/esped/.cache/kagglehub/datasets/olistbr/brazilian-ecommerce/versions/2

    diretorio_delete:
    C:/Users/esped/.cache/kagglehub/datasets/
    """

    # Converte o caminho recebido para Path.
    # O strip() remove espaços acidentais no início ou no fim do caminho.
    cache_dir = Path(str(cache_dir).strip())

    parts = cache_dir.parts

    if "datasets" not in parts:
        print("A pasta 'datasets' não foi encontrada no caminho do cache.")
        print(f"Caminho recebido: {cache_dir}")
        return

    datasets_index = parts.index("datasets")

    diretorio_delete = Path(*parts[: datasets_index + 1])

    if not diretorio_delete.exists():
        print(f"O diretório não existe: {diretorio_delete}")
        return

    shutil.rmtree(diretorio_delete)

    print(f"Diretório removido com sucesso: {diretorio_delete}")


def download_raw_data() -> None:
    """
    Baixa o conjunto de dados Brazilian E-Commerce do Kaggle
    e move os arquivos para o diretório data/raw/ do projeto.

    Depois de mover os arquivos, remove todos os arquivos e pastas
    dentro de cache/kagglehub/datasets.
    """
    dataset_name = "olistbr/brazilian-ecommerce"

    print("Iniciando o download do dataset do Kaggle...")

    try:
        cache_path = kagglehub.dataset_download(dataset_name)

    except Exception as error:
        raise RuntimeError(
            f"Erro ao baixar o dataset '{dataset_name}' do Kaggle."
        ) from error

    cache_dir = Path(cache_path)

    if not cache_dir.exists():
        raise FileNotFoundError(f"O diretório de cache não foi encontrado: {cache_dir}")

    print(f"Arquivos baixados no cache: {cache_dir}")

    project_root = Path(__file__).resolve().parents[2]

    target_dir = project_root / "data" / "raw"
    target_dir.mkdir(parents=True, exist_ok=True)

    print(f"Movendo arquivos para: {target_dir}")

    moved_files = 0

    for file_path in cache_dir.iterdir():
        if not file_path.is_file():
            continue

        target_file = target_dir / file_path.name

        shutil.move(str(file_path), str(target_file))

        moved_files += 1
        print(f" - Movido: {file_path.name}")

    if moved_files == 0:
        print("Nenhum arquivo foi encontrado para mover.")

    else:
        print("\nDownload e organização concluídos com sucesso!")
        print(f"Total de arquivos movidos: {moved_files}")

    clear_kagglehub_datasets_cache(cache_dir)


if __name__ == "__main__":
    download_raw_data()