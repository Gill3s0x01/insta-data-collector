import instaloader


def buscar_dados_instagram(username):
    L = instaloader.Instaloader()

    try:
        profile = instaloader.Profile.from_username(L.context, username)

        dados = {
            "User ID": profile.userid,
            "Username": profile.username,
            "Full Name": profile.full_name,
            "Bio": profile.biography,
            "External URL": profile.external_url,
            "Is Verified": profile.is_verified,
            "Is Private": profile.is_private,
            "Followers": profile.followers,
            "Followees": profile.followees,
            "Number of Posts": profile.mediacount,
            "Profile Picture URL": profile.profile_pic_url,
            "Email": "Não disponível via API pública",
            "Phone": "Não disponível via API pública",
        }

        return dados

    except Exception as e:
        return {"Erro": str(e)}


if __name__ == "__main__":
    username = input("Digite o nome do perfil Instagram que deseja buscar: ").strip()
    dados = buscar_dados_instagram(username)

    for chave, valor in dados.items():
        print(f"{chave}: {valor}")
