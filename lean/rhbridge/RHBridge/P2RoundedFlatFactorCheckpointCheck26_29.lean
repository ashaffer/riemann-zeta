import RHBridge.P2RoundedFlatFactorCheckpointData26

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FlatComponentChunk29 :
    P2RoundedFactorCheckpointData.panel26FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get ⟨5, by decide⟩ := by
  decide +kernel

theorem panel26FlatOdd5_eq :
    P2RoundedFactorCheckpointData.panel26FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get ⟨5, by decide⟩ := by
  exact panel26FlatComponentChunk29

end RHP2Bridge
