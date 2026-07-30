import RHBridge.P2RoundedFactorCheckpointData4

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FactorChunk1 :
    P2RoundedFactorCheckpointData.panel4Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨4, by decide⟩ := by
  decide +kernel

theorem panel4Prefix4_eq :
    P2RoundedFactorCheckpointData.panel4Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk1.1

theorem panel4Prefix5_eq :
    P2RoundedFactorCheckpointData.panel4Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk1.2.1

theorem panel4Prefix6_eq :
    P2RoundedFactorCheckpointData.panel4Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk1.2.2.1

theorem panel4Prefix7_eq :
    P2RoundedFactorCheckpointData.panel4Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk1.2.2.2

end RHP2Bridge
