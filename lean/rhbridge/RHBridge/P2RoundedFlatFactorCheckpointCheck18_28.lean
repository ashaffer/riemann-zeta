import RHBridge.P2RoundedFlatFactorCheckpointData18

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FlatComponentChunk28 :
    P2RoundedFactorCheckpointData.panel18FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get ⟨4, by decide⟩ := by
  decide +kernel

theorem panel18FlatOdd4_eq :
    P2RoundedFactorCheckpointData.panel18FlatOdd4 =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get ⟨4, by decide⟩ := by
  exact panel18FlatComponentChunk28

end RHP2Bridge
