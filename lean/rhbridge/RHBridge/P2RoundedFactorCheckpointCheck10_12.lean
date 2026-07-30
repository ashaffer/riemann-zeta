import RHBridge.P2RoundedFactorCheckpointData10

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FactorChunk12 :
    P2RoundedFactorCheckpointData.panel10Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨10, by decide⟩ := by
  decide +kernel

theorem panel10Prefix48_eq :
    P2RoundedFactorCheckpointData.panel10Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk12.1

theorem panel10Prefix49_eq :
    P2RoundedFactorCheckpointData.panel10Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk12.2.1

theorem panel10Prefix50_eq :
    P2RoundedFactorCheckpointData.panel10Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk12.2.2.1

theorem panel10Prefix51_eq :
    P2RoundedFactorCheckpointData.panel10Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk12.2.2.2

end RHP2Bridge
