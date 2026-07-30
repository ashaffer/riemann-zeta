import RHBridge.P2RoundedFlatFactorCheckpointData1

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FlatComponentChunk11 :
    P2RoundedFactorCheckpointData.panel1FlatEven11 =
      (P2RoundedFactorCheckpointData.panel1TruncatedEvenComponents).get ⟨11, by decide⟩ := by
  decide +kernel

theorem panel1FlatEven11_eq :
    P2RoundedFactorCheckpointData.panel1FlatEven11 =
      (P2RoundedFactorCheckpointData.panel1TruncatedEvenComponents).get ⟨11, by decide⟩ := by
  exact panel1FlatComponentChunk11

end RHP2Bridge
