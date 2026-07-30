import RHBridge.P2RoundedFlatFactorCheckpointData18

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FlatComponentChunk15 :
    P2RoundedFactorCheckpointData.panel18FlatEven15 =
      (P2RoundedFactorCheckpointData.panel18TruncatedEvenComponents).get ⟨15, by decide⟩ := by
  decide +kernel

theorem panel18FlatEven15_eq :
    P2RoundedFactorCheckpointData.panel18FlatEven15 =
      (P2RoundedFactorCheckpointData.panel18TruncatedEvenComponents).get ⟨15, by decide⟩ := by
  exact panel18FlatComponentChunk15

end RHP2Bridge
