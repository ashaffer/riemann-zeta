import RHBridge.P2RoundedFlatFactorCheckpointData13

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FlatComponentChunk39 :
    P2RoundedFactorCheckpointData.panel13FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨15, by decide⟩ := by
  decide +kernel

theorem panel13FlatOdd15_eq :
    P2RoundedFactorCheckpointData.panel13FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨15, by decide⟩ := by
  exact panel13FlatComponentChunk39

end RHP2Bridge
