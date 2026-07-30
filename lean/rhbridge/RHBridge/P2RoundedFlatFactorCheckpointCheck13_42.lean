import RHBridge.P2RoundedFlatFactorCheckpointData13

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FlatComponentChunk42 :
    P2RoundedFactorCheckpointData.panel13FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨18, by decide⟩ := by
  decide +kernel

theorem panel13FlatOdd18_eq :
    P2RoundedFactorCheckpointData.panel13FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel13TruncatedOddComponents).get ⟨18, by decide⟩ := by
  exact panel13FlatComponentChunk42

end RHP2Bridge
