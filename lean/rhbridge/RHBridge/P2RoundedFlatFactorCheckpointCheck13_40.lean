import RHBridge.P2RoundedFlatFactorCheckpointData13

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FlatComponentChunk40 :
    P2RoundedFactorCheckpointData.panel13FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨16, by decide⟩ := by
  decide +kernel

theorem panel13FlatOdd16_eq :
    P2RoundedFactorCheckpointData.panel13FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨16, by decide⟩ := by
  exact panel13FlatComponentChunk40

end RHP2Bridge
