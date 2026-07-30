import RHBridge.P2RoundedFlatFactorCheckpointData2

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FlatComponentChunk1 :
    P2RoundedFactorCheckpointData.panel2FlatEven1 =
      (P2RoundedFactorCheckpointData.panel2TruncatedEvenComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel2FlatEven1_eq :
    P2RoundedFactorCheckpointData.panel2FlatEven1 =
      (P2RoundedFactorCheckpointData.panel2TruncatedEvenComponents).get ⟨1, by decide⟩ := by
  exact panel2FlatComponentChunk1

end RHP2Bridge
