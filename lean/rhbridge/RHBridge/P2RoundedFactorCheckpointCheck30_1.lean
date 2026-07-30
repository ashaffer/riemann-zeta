import RHBridge.P2RoundedFactorCheckpointData30

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FactorChunk1 :
    P2RoundedFactorCheckpointData.panel30Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨30, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel30Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨30, by decide⟩ := by
  decide +kernel

theorem panel30Prefix4_eq :
    P2RoundedFactorCheckpointData.panel30Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk1.1

theorem panel30Prefix5_eq :
    P2RoundedFactorCheckpointData.panel30Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk1.2.1

theorem panel30Prefix6_eq :
    P2RoundedFactorCheckpointData.panel30Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk1.2.2.1

theorem panel30Prefix7_eq :
    P2RoundedFactorCheckpointData.panel30Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨30, by decide⟩ := by
  exact panel30FactorChunk1.2.2.2

end RHP2Bridge
