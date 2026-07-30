import RHBridge.P2RoundedFactorCheckpointData6

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel6FactorChunk4 :
    P2RoundedFactorCheckpointData.panel6Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨6, by decide⟩ := by
  decide +kernel

theorem panel6Prefix16_eq :
    P2RoundedFactorCheckpointData.panel6Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk4.1

theorem panel6Prefix17_eq :
    P2RoundedFactorCheckpointData.panel6Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk4.2.1

theorem panel6Prefix18_eq :
    P2RoundedFactorCheckpointData.panel6Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk4.2.2.1

theorem panel6Prefix19_eq :
    P2RoundedFactorCheckpointData.panel6Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk4.2.2.2

end RHP2Bridge
