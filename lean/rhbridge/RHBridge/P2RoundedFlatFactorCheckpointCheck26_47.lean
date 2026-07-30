import RHBridge.P2RoundedFlatFactorCheckpointData26

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FlatComponentChunk47 :
    P2RoundedFactorCheckpointData.panel26FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get ⟨23, by decide⟩ := by
  decide +kernel

theorem panel26FlatOdd23_eq :
    P2RoundedFactorCheckpointData.panel26FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get ⟨23, by decide⟩ := by
  exact panel26FlatComponentChunk47

end RHP2Bridge
