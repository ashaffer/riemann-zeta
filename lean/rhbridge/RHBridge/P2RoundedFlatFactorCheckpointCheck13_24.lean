import RHBridge.P2RoundedFlatFactorCheckpointData13

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FlatComponentChunk24 :
    P2RoundedFactorCheckpointData.panel13FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨0, by decide⟩ := by
  decide +kernel

theorem panel13FlatOdd0_eq :
    P2RoundedFactorCheckpointData.panel13FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨0, by decide⟩ := by
  exact panel13FlatComponentChunk24

end RHP2Bridge
