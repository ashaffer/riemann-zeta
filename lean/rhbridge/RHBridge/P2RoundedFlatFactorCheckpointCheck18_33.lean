import RHBridge.P2RoundedFlatFactorCheckpointData18

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FlatComponentChunk33 :
    P2RoundedFactorCheckpointData.panel18FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get ⟨9, by decide⟩ := by
  decide +kernel

theorem panel18FlatOdd9_eq :
    P2RoundedFactorCheckpointData.panel18FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get ⟨9, by decide⟩ := by
  exact panel18FlatComponentChunk33

end RHP2Bridge
