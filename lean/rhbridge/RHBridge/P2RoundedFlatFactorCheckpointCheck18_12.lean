import RHBridge.P2RoundedFlatFactorCheckpointData18

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FlatComponentChunk12 :
    P2RoundedFactorCheckpointData.panel18FlatEven12 =
      (P2RoundedFactorCheckpointData.panel18TruncatedEvenComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel18FlatEven12_eq :
    P2RoundedFactorCheckpointData.panel18FlatEven12 =
      (P2RoundedFactorCheckpointData.panel18TruncatedEvenComponents).get ⟨12, by decide⟩ := by
  exact panel18FlatComponentChunk12

end RHP2Bridge
