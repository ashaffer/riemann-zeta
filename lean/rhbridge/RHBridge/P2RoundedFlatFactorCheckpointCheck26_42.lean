import RHBridge.P2RoundedFlatFactorCheckpointData26

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FlatComponentChunk42 :
    P2RoundedFactorCheckpointData.panel26FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get ⟨18, by decide⟩ := by
  decide +kernel

theorem panel26FlatOdd18_eq :
    P2RoundedFactorCheckpointData.panel26FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get ⟨18, by decide⟩ := by
  exact panel26FlatComponentChunk42

end RHP2Bridge
