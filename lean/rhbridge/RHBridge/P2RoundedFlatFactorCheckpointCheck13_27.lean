import RHBridge.P2RoundedFlatFactorCheckpointData13

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FlatComponentChunk27 :
    P2RoundedFactorCheckpointData.panel13FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel13FlatOdd3_eq :
    P2RoundedFactorCheckpointData.panel13FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨3, by decide⟩ := by
  exact panel13FlatComponentChunk27

end RHP2Bridge
