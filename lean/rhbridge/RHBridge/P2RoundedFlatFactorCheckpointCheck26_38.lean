import RHBridge.P2RoundedFlatFactorCheckpointData26

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FlatComponentChunk38 :
    P2RoundedFactorCheckpointData.panel26FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get ⟨14, by decide⟩ := by
  decide +kernel

theorem panel26FlatOdd14_eq :
    P2RoundedFactorCheckpointData.panel26FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get ⟨14, by decide⟩ := by
  exact panel26FlatComponentChunk38

end RHP2Bridge
