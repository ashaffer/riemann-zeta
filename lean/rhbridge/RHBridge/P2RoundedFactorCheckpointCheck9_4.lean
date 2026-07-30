import RHBridge.P2RoundedFactorCheckpointData9

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FactorChunk4 :
    P2RoundedFactorCheckpointData.panel9Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨9, by decide⟩ := by
  decide +kernel

theorem panel9Prefix16_eq :
    P2RoundedFactorCheckpointData.panel9Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk4.1

theorem panel9Prefix17_eq :
    P2RoundedFactorCheckpointData.panel9Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk4.2.1

theorem panel9Prefix18_eq :
    P2RoundedFactorCheckpointData.panel9Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk4.2.2.1

theorem panel9Prefix19_eq :
    P2RoundedFactorCheckpointData.panel9Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk4.2.2.2

end RHP2Bridge
