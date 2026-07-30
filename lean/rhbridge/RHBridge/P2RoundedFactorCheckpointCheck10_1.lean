import RHBridge.P2RoundedFactorCheckpointData10

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10FactorChunk1 :
    P2RoundedFactorCheckpointData.panel10Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨10, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel10Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨10, by decide⟩ := by
  decide +kernel

theorem panel10Prefix4_eq :
    P2RoundedFactorCheckpointData.panel10Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk1.1

theorem panel10Prefix5_eq :
    P2RoundedFactorCheckpointData.panel10Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk1.2.1

theorem panel10Prefix6_eq :
    P2RoundedFactorCheckpointData.panel10Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk1.2.2.1

theorem panel10Prefix7_eq :
    P2RoundedFactorCheckpointData.panel10Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨10, by decide⟩ := by
  exact panel10FactorChunk1.2.2.2

end RHP2Bridge
