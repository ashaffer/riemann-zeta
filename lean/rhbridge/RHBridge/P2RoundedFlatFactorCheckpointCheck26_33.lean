import RHBridge.P2RoundedFlatFactorCheckpointData26

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FlatComponentChunk33 :
    P2RoundedFactorCheckpointData.panel26FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get ⟨9, by decide⟩ := by
  decide +kernel

theorem panel26FlatOdd9_eq :
    P2RoundedFactorCheckpointData.panel26FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get ⟨9, by decide⟩ := by
  exact panel26FlatComponentChunk33

end RHP2Bridge
