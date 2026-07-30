import RHBridge.P2RoundedFlatFactorCheckpointData18

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FlatComponentChunk23 :
    P2RoundedFactorCheckpointData.panel18FlatEven23 =
      (P2RoundedFactorCheckpointData.panel18TruncatedEvenComponents).get ⟨23, by decide⟩ := by
  decide +kernel

theorem panel18FlatEven23_eq :
    P2RoundedFactorCheckpointData.panel18FlatEven23 =
      (P2RoundedFactorCheckpointData.panel18TruncatedEvenComponents).get ⟨23, by decide⟩ := by
  exact panel18FlatComponentChunk23

end RHP2Bridge
